import random
import streamlit as st

# Function for Rock, Paper, Scissors Game
def rock_paper_scissors():
    # Function to show the game interface and result
    def main():
        # Title for the game
        st.markdown('<h1 class="title">🪐 Rock, Paper, Scissors Game 🪐</h1>', unsafe_allow_html=True)

        # Instructions Section
        st.markdown('<p class="instructions">Choose between Rock, Paper, or Scissors and let\'s see who wins!</p>', unsafe_allow_html=True)

        # Create columns for the user and computer choices
        col1, col2 = st.columns(2)

        with col1:
            # User choice with icons
            user_choice = st.radio("Your choice:", ["🪨 Rock", "📄 Paper", "✂ Scissors"], key="user_choice", index=0)

        # Generate computer's choice
        comp_choice_num = random.randint(1, 3)
        comp_choice = ["🪨 Rock", "📄 Paper", "✂ Scissors"][comp_choice_num - 1]

        with col2:
            # Display the computer's choice with a little delay for effect
            st.markdown(f'<div class="choice">Computer\'s choice: {comp_choice}</div>', unsafe_allow_html=True)

        # Determine the result
        if user_choice == comp_choice:
            result = "DRAW"
        elif (user_choice == "🪨 Rock" and comp_choice == "✂ Scissors") or \
             (user_choice == "✂ Scissors" and comp_choice == "📄 Paper") or \
             (user_choice == "📄 Paper" and comp_choice == "🪨 Rock"):
            result = "You win!"
        else:
            result = "Computer wins!"

        # Show the result with styling
        st.markdown(f'<div class="result">{result}</div>', unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align: center; font-size: 12px;'>By Team STAR</p>", 
            unsafe_allow_html=True
        )

    main()

# Function for Guess the 3-Digit Number Game
def guess_the_number():
    if 'num' not in st.session_state:
        st.session_state.num = random.randrange(100, 1000)  # Generate the random 3-digit number
        st.session_state.ctr = 0  # Initialize attempt counter
        st.session_state.correct_guess = False  # Track if the guess is correct
        st.session_state.game_over = False  # Flag to indicate if the game is over

    # Display game title with additional styling
    st.title("🎯 Guess the 3-Digit Number! 🎯")
    st.write("Try to guess the 3-digit number. You will get feedback on how many digits you guessed correctly. 🔢")

    # Add a bit of space between the game info and the input form
    st.write("\n" * 2)  # Adds 2 newlines for spacing

    # If the game is over, display the Restart Game button
    if st.session_state.game_over:
        st.write("Congratulations! 🎉 You've guessed the number correctly!")
        st.write(f"It took you {st.session_state.ctr} tries to guess the number. 🏆")
        st.write("\n")  # Adds a newline for spacing between the message and the button
        if st.button("🔄 Restart Game"):
            # Reset the game state
            st.session_state.num = random.randrange(100, 1000)  # Generate a new random number
            st.session_state.ctr = 0  # Reset attempt counter
            st.session_state.correct_guess = False  # Reset correct guess flag
            st.session_state.game_over = False  # Reset game over flag
            st.session_state.guess = None  # Reset last guess

    # If the game is not over, continue to make guesses
    if not st.session_state.game_over:
        st.write("Your current guess attempt:")
        # Get user input for guessing the number
        guess = st.number_input(
            "🔢 Enter your guess (3 digits):", 
            min_value=100, 
            max_value=999, 
            step=1, 
            key="guess",
            format="%d"  # Ensure the format is integer (3 digits)
        )

        # If the user provides a guess, process it
        if guess:
            st.session_state.ctr += 1  # Increment the counter for each guess
            n_str = str(guess)
            num_str = str(st.session_state.num)

            count = 0
            correct = ['X'] * 3  # List with 3 placeholders for the digits

            # Check each digit of the guess
            for i in range(3):
                if n_str[i] == num_str[i]:
                    count += 1
                    correct[i] = n_str[i]

            # Provide feedback based on the number of correct digits
            if count == 3:
                st.session_state.correct_guess = True
                st.write("🎉 You've guessed the number correctly! 🎉")
                st.write(f"It took you {st.session_state.ctr} tries to guess the number. 🏆")
                st.session_state.game_over = True  # End the game
            else:
                if count > 0:
                    st.write(f"🔍 Not quite the number. But you did get {count} digit(s) correct! ✅")
                else:
                    st.write("❌ None of the numbers in your input match. Try again! 🎯")

        else:
            st.write("⚠ Please enter a valid 3-digit number.")

    # Add some space after the game interaction
    st.write("\n" * 2)  # Adds more space between sections

# Function for Tic-Tac-Toe Game
def tic_tac_toe():
    import streamlit as st
    import random

    # Function to initialize the game state
    def initialize_game():
        return [['' for _ in range(3)] for _ in range(3)], '❌'  # '❌' for X (Player), '⭕' for O (Computer)

    # Function to check if there is a winner
    def check_winner(board):
        for i in range(3):
            # Check rows and columns
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
                return board[0][i]

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
            return board[0][2]

        return None

    # Function to render the board with clickable buttons
    def render_board():
        board = st.session_state['board']
        for i in range(3):
            cols = st.columns(3)  # Create 3 columns for the row
            for j in range(3):
                button_label = board[i][j] if board[i][j] != '' else ' '
                with cols[j]:
                    if st.button(button_label, key=f"{i}-{j}", help="Click to make your move"):
                        return i, j  # Return the position when the button is clicked
        return None, None

    # Function for the computer to make a move
    def computer_move():
        board = st.session_state['board']
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
        if empty_cells:
            return random.choice(empty_cells)
        return None, None  # In case there are no empty cells left (game over)

    # Main function to handle game logic
    def main():
        st.title("Tic-Tac-Toe Game 🎮")

        # Initialize game state if not already in session_state
        if 'board' not in st.session_state:
            st.session_state['board'], st.session_state['turn'] = initialize_game()

        # Display the current player's turn
        st.markdown(f"Current Turn: {st.session_state['turn']} 🕹")
        
        # Render the Tic-Tac-Toe board and capture the move
        i, j = render_board()

        # Game logic to process the move
        if i is not None and j is not None:  # When a valid move is made by the player
            if st.session_state['board'][i][j] == '':  # Ensure the cell is empty before marking
                st.session_state['board'][i][j] = st.session_state['turn']
                # Check for winner
                winner = check_winner(st.session_state['board'])
                if winner:
                    st.success(f"🎉 {winner} Wins! 🏆")
                    st.session_state['board'], st.session_state['turn'] = initialize_game()  # Reset game after win
                else:
                    # Switch turn to the computer ('⭕')
                    st.session_state['turn'] = '⭕'
                

        # If it's the computer's turn
        if st.session_state['turn'] == '⭕':
            # Let the computer make a move
            i, j = computer_move()
            if i is not None and j is not None:
                st.session_state['board'][i][j] = '⭕'
                # Check for winner after the computer's move
                winner = check_winner(st.session_state['board'])
                if winner:
                    st.success(f"🎉 {winner} Wins! 🏆")
                    st.session_state['board'], st.session_state['turn'] = initialize_game()  # Reset game after win
                else:
                    # Switch turn to the player ('❌')
                    st.session_state['turn'] = '❌'

        # Option to reset the game
        if st.button("🔄 Reset Game"):
            st.session_state['board'], st.session_state['turn'] = initialize_game()

    # Run the game
    main()

# Main function to handle the dropdown and game display
def main():
    st.sidebar.title("Games")
    selected_game = st.sidebar.selectbox("Select a game:", ["Rock, Paper, Scissors", "Guess the Number", "Tic-Tac-Toe"])

    if selected_game == "Rock, Paper, Scissors":
        rock_paper_scissors()
    elif selected_game == "Guess the Number":
        guess_the_number()
    elif selected_game == "Tic-Tac-Toe":
        tic_tac_toe()

# Run the main function
if __name__ == "__main__":
    main()