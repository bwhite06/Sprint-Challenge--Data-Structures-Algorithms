class Building:
  def __init__(self,story):
    self.story = story
    self._f_= .010
  def minimize_eggs_drop(self,story): 
      height=story*3.3
      weight = 50
      G = 9.8
      breakheight = .010
      PotentialEnegry = weight*G*height
      safePotentialEngergy = weight*G*breakheight
      n = safePotentialEngergy-PotentialEnegry

      if n<0.0049:
          print("egg will crush",n)
      else:
         print("egg survives",n)
  def egg_crush(self):
      empire_state.minimize_eggs_drop(self.story)

empire_state = Building(.0000009999)
print(empire_state.egg_crush())