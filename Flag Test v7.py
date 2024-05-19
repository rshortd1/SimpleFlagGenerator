import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from PIL import ImageTk, Image

def generate_flag():
    flag = np.zeros((100, 200, 3))  # Initialize flag with zeros
    
    # Generate random number to decide flag type
    flag_type = np.random.random()
    
    if flag_type < 0.10:  # 10% chance of split vertically
        color1 = np.random.rand(3)  # Random color 1
        color2 = np.random.rand(3)  # Random color 2
        flag[:, :100] = color1  # Left half
        flag[:, 100:] = color2  # Right half
    
    elif flag_type < 0.30:  # 20% chance of split horizontally
        color1 = np.random.rand(3)  # Random color 1
        color2 = np.random.rand(3)  # Random color 2
        flag[:50, :] = color1  # Top half
        flag[50:, :] = color2  # Bottom half
    
    elif flag_type < 0.40:  # 10% chance of split diagonally
        color1 = np.random.rand(3)  # Random color 1
        color2 = np.random.rand(3)  # Random color 2
        for i in range(100):
            for j in range(200):
                if i > j:
                    flag[i, j] = color1
                else:
                    flag[i, j] = color2
    
    elif flag_type < 0.50:  # 10% chance of split into triangles
        color1 = np.random.rand(3)  # Random color 1
        color2 = np.random.rand(3)  # Random color 2
        for i in range(100):
            for j in range(200):
                if i <= j:
                    flag[i, j] = color1
                else:
                    flag[i, j] = color2
    
    elif flag_type < 0.55:  # Adjusted for the new range
        colors = [np.random.rand(3) for _ in range(3)]  # Generate random colors
        flag[:, :67] = colors[0]  # First third
        flag[:, 67:133] = colors[1]  # Second third
        flag[:, 133:] = colors[2]  # Third third
    
    elif flag_type < 0.60:  # 10% chance of a gradient flag
        color1 = np.random.rand(3)  # Random color 1
        color2 = np.random.rand(3)  # Random color 2
        for i in range(100):
            for j in range(200):
                flag[i, j] = (color2 - color1) * (i / 100) + color1
    
    elif flag_type < 0.65:  # 10% chance of a checkered board flag
        color1 = np.random.rand(3)  # Random color 1
        color2 = np.random.rand(3)  # Random color 2
        for i in range(10):  # 10 rows
            for j in range(20):  # 20 columns
                if (i + j) % 2 == 0:
                    flag[i*10:(i+1)*10, j*10:(j+1)*10] = color1
                else:
                    flag[i*10:(i+1)*10, j*10:(j+1)*10] = color2
    
    elif flag_type < 0.80:  # 15% chance of equal 3 colors split horizontally
        colors = [np.random.rand(3) for _ in range(3)]  # Generate random colors
        flag[:33, :] = colors[0]  # First third
        flag[33:66, :] = colors[1]  # Second third
        flag[66:, :] = colors[2]  # Third third
    
    else:  # Rest of the cases
        color = np.random.rand(3)  # Random color
        flag[:, :] = color  # Single color
        
        # Symbol chance split
        symbol_chance = np.random.random()
        symbols = ['o', 's', '^', 'D', 'v', '*', 'h','U','M']  # Available symbols
        symbol = np.random.choice(symbols)  # Choose a random symbol
        
        if symbol_chance < 0.75:  # 75% chance of one symbol
            plt.text(100, 50, symbol, fontsize=97.5, weight='bold', ha='center', va='center', color='white')  # Add symbol at the center
        else:  # 25% chance of two symbols
            symbol2 = np.random.choice(symbols)
            plt.text(90, 50, symbol, fontsize=97.5, weight='bold', ha='center', va='center', color='white')  # First symbol
            plt.text(110, 50, symbol2, fontsize=97.5, weight='bold', ha='center', va='center', color='white')  # Second symbol
        
    return flag

def display_flag(flag):
    plt.imshow(flag)
    plt.axis('off')
    plt.show()

def regenerate_flag():
    flag = generate_flag()
    display_flag(flag)

if __name__ == "__main__":
    flag = generate_flag()
    display_flag(flag)
    
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Flag Generator")
    
    # Generate button
    generate_button = tk.Button(window, text="Regenerate Flag", command=regenerate_flag)
    generate_button.pack(pady=10)
    
    # Display the flag in the window
    flag_image = ImageTk.PhotoImage(Image.fromarray((flag * 255).astype(np.uint8)))
    flag_label = tk.Label(window, image=flag_image)
    flag_label.pack()
    
    # Run the Tkinter event loop
    window.mainloop()
