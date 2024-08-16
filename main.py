# main.py

import os
from gui import CreditCardCalculatorGUI

def main():
    """
    The main function to run the Credit Card Calculator application.
    It initializes and runs the GUI.
    """
    os.environ['TK_SILENCE_DEPRECATION'] = '1'
    
    # Create the GUI object
    calculator_gui = CreditCardCalculatorGUI()
    
    # Run the GUI application
    calculator_gui.run()

if __name__ == "__main__":
    main()

