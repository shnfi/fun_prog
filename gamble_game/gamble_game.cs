using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

namespace GambleGame
{
    class Program
    {
        static void Main(string[] args)
        {

            int money = 100;

            while (true)
            {
                Random rnd = new Random();
                string slot1, slot2, slot3;
                List<string> slots = new List<string> { "A", "B", "C", "D"};
                List<int> moneyTimes = new List<int> { -5, 5, 10 };


                sayYourMoney(money);

                Console.Write("Enter your Gamble Money > ");
                int moneyIn = Convert.ToInt32(Console.ReadLine());

                if (moneyIn > money)
                {
                    Console.WriteLine("It's Greater than Your Money !!");
                    sleep(1500);
                    System.Environment.Exit(1);
                }

                money -= moneyIn;

                slot1 = slots[rnd.Next(0, 4)];
                slot2 = slots[rnd.Next(0, 4)];
                slot3 = slots[rnd.Next(0, 4)];

                Console.WriteLine();

                Console.WriteLine("3");
                sleep(1000);

                Console.WriteLine("2");
                sleep(1000);

                Console.WriteLine("1");
                sleep(1000);

                Console.Clear();

                Console.WriteLine("----------");
                Console.WriteLine(slot1 + " | " + slot2 + " | " + slot3);
                Console.WriteLine("----------");

                if (slot1 == slot2 && slot2 == slot3)
                {
                    money += (moneyIn * moneyTimes[2]);
                }
                else if (slot1 == slot2 && slot2 != slot3 || slot2 == slot3 && slot1 != slot3 || slot1 == slot3 && slot2 != slot3)
                {
                    money += (moneyIn * moneyTimes[1]);
                }
                else if (slot1 != slot2 && slot2 != slot3)
                {
                    money += 0;
                }

                if (money < 1)
                {
                    Console.WriteLine("Your Money is Less than 1$ !!");
                    sleep(1500);
                    System.Environment.Exit(1);
                }

                sayYourMoney(money);

                sleep(2500);

                Console.Clear();
            }




            Console.ReadKey();
        }




        static void sayYourMoney(int money)
        {

            Console.WriteLine("[$] Your Cash is -> " + money + "$");
        }



        static void sleep(int sec)
        {

            System.Threading.Thread.Sleep(sec);
        }

    }
}
