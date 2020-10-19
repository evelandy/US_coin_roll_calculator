def main():
      deco = '=' * 50
      choice = input("do you want to enter [p] pounds or [g] grams? ")
      if choice.lower() == 'p':
            total_penny_weight = float(input("enter the total weight of the pennies you have: "))
            total_nickel_weight = float(input("enter the total weight of the nickels you have: "))
            total_dime_weight = float(input("enter the total weight of the dimes you have: "))
            total_quarter_weight = float(input("enter the total weight of the quarters you have: "))
            total_penny_weight *= 453.59
            total_nickel_weight *= 453.59
            total_dime_weight *= 453.59
            total_quarter_weight *= 453.59
      elif choice.lower() == 'g':
            total_penny_weight = float(input("enter the total weight of the pennies you have: "))
            total_nickel_weight = float(input("enter the total weight of the nickels you have: "))
            total_dime_weight = float(input("enter the total weight of the dimes you have: "))
            total_quarter_weight = float(input("enter the total weight of the quarters you have: "))

      print(deco)
      penny = pennies(total_penny_weight)
      print(deco)
      nickel = nickels(total_nickel_weight)
      print(deco)
      dime = dimes(total_dime_weight)
      print(deco)
      quarter = quarters(total_quarter_weight)
      print(deco)
      total_money = "Your total valued money is about ${}".format(format(float(quarter) + float(dime) + float(nickel) + float(penny), '.2f'))
      print(total_money)


def pennies(total_penny_weight):
      penny_weight_grams = 2.500
      penny_roll = 50
      penny_value = .01
      total_pennies = round(total_penny_weight / penny_weight_grams)
      total_penny_value = format(total_pennies * penny_value, '.2f')
      total_penny_rolls = round(total_pennies / penny_roll)
      print("You have about {} pennies. \nValued at about ${} \nYou will need about {} " \
             "roll(s)".format(total_pennies, total_penny_value, total_penny_rolls))
      return total_penny_value


def nickels(total_nickel_weight):
      nickel_weight_grams = 5.000
      nickel_roll = 40
      nickel_value = .05
      total_nickels = round(total_nickel_weight / nickel_weight_grams)
      total_nickel_value = format(total_nickels * nickel_value, '.2f')
      total_nickel_rolls = round(total_nickels / nickel_roll)
      print("You have {} nickels. \nValued at ${} \nYou will need about {} " \
             "roll(s)".format(total_nickels, total_nickel_value, total_nickel_rolls))
      return total_nickel_value


def dimes(total_dime_weight):
      dime_weight_grams = 2.268
      dime_roll = 50
      dime_value = .10
      total_dimes = round(total_dime_weight / dime_weight_grams)
      total_dime_value = format(total_dimes * dime_value, '.2f')
      total_dime_rolls = round(total_dimes / dime_roll)
      print("You have {} dimes. \nValued at ${} \nYou will need about {} " \
             "roll(s)".format(total_dimes, total_dime_value, total_dime_rolls))
      return total_dime_value


def quarters(total_quarter_weight):
      quarter_weight_grams = 5.670
      quarter_roll = 40
      quarter_value = .25
      total_quarters = round(total_quarter_weight / quarter_weight_grams)
      total_quarter_value = format(total_quarters * quarter_value, '.2f')
      total_quarter_rolls = round(total_quarters / quarter_roll)
      print("You have {} quarters. \nValued at ${} \nYou will need about {} " \
             "roll(s)".format(total_quarters, total_quarter_value, total_quarter_rolls))
      return total_quarter_value


if__name__ == "__main__":
    main()
