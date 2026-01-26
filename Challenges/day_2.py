"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key 
details and generates a short, stylish bio that could be
 used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. 
It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""

name = input("What's your name? ").strip()
profession = input("What's your profession? ").strip()
passion = input("What's your spark? ").strip()
emoji = input("What's your favorite emoji? ").strip()
website = input("Where to find you? ").strip()

format_1 = f"{emoji} {name} | {profession}\n{passion}\n{website}"
format_2 = f"{emoji} {name} \n💼{profession}\n💥{passion}\n🔗{website}"
format_3 = f"{emoji} {name} the {profession}.\n{passion}\nGet in touch: {website}"

print(f"\n1.{format_1}\n\n2.{format_2}\n\n3.{format_3}\n\n")
format_choice = input("Which format would you like for your bio? ")

if format_choice == "1":
    bio = format_1
elif format_choice == "2":
    bio = format_2
else:
    bio = format_3
    
save = input("Do you want to save your bio to a file? (yes/no) ").lower().strip()

if save == "yes" or save == "y":
    filename = f"{name.lower().replace(' ','_')}_bio.txt" 
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print(f"Bio saved to {filename}")