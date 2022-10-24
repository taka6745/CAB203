import re


def censor(s):
   articles = ['a', 'an','the']
   def replace(match):
      word = match.group()
      if word.lower() in articles:
         return '#' * len(word)
      else:
         return word
   r = re.sub(r'\b\w*\b', replace, s, flags=re.I|re.U|re.IGNORECASE)
   if r == s: return r
   else: return r + " <n10999795>"
   


def makeBet(headsOdds, tailsOdds, previousOutcome, state):
   if previousOutcome == None:
      state = {"biasHeadOdds": 0.5, "biasTailOdds": 0.5, "probHead": 0.55, "probTail": 0.45, "heads": 0,"tails":0}
   elif previousOutcome == 'heads':
      state["heads"] += 1
   elif previousOutcome == 'tails':
      state["tails"] += 1

   state["biasHeadOdds"] = ((0.7**state['heads']*0.3**state['tails'])/state['biasHeadOdds'])/((1*0.4**state['heads']+1*0.7**state['heads'])/2)
   state["biasTailOdds"] = ((0.6**state['tails']*0.3**state['heads'])/state['biasTailOdds'])/((1*0.3**state['tails']+1*0.6**state['tails'])/2)
   state['probHead'] = (0.7*state["biasHeadOdds"])+(0.4*state["biasTailOdds"])
   state['probTail'] = (0.3*state["biasHeadOdds"])+(0.6*state["biasTailOdds"]) # has to be done twice because the larger variable will switch around 
   profitHead = (headsOdds*state['probHead'])+((-1)*state['probTail'])
   profitTail = (tailsOdds*state['probTail'])+((-1)*state['probHead'])
   noBet = 0
   if (profitHead > profitTail and profitHead > noBet):
      bet = "heads"
   elif profitTail > profitHead and profitTail > noBet:
      bet = "tails"
   else:
      bet = 'no bet'
   
   return (bet, state)


# The following will be run if you execute the file like python3 problem_solving.py
# Your solutions should not depend on this code.
# The automated marker will ignore any changes to this code; feel free to modify it
# but keep the if and the indenting as is
if __name__ == '__main__':
   try:
      print(censor('The cat ate a mouse.')) # should give "### cat ate # mouse. <n1234567>"
   except NameError:
      print("Not attempting censoring problem")
   try:
      print(fertiliser(1, 0, 0, 1, 2, 2)) # should give (2.0, 2.0)
   except NameError:
      print("Not attempting fertiliser problem")

   import random
   try:
      random.seed(0)
      totalprofit = 0
      for round in range(10000):
         if random.randint(0,1) == 0:
            headsprob = 0.7
         else:
            headsprob = 0.4

         previousOutcome = None
         state = None
         profit = 0
         odds = dict()
         for _ in range(100):
            odds['heads'] = random.uniform(1, 3)
            odds['tails'] = random.uniform(1, 3)
            
            bet, state = makeBet(odds['heads'], odds['tails'], previousOutcome, state)
            
            previousOutcome = 'heads' if random.random() < headsprob else 'tails'
            if bet == previousOutcome:
               profit += odds[bet] - 1
            elif bet != 'no bet':
               profit -= 1          # stake lost

         print("Probability of heads was", headsprob, "Profit was", profit)
         totalprofit += profit
      print("Average profit per run:", totalprofit / 10000)

   except NameError as e:
      print("Not attempting probability problem")