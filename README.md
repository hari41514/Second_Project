# About This Project:

This project is a **Number Guessing Game** built as a web application using the Flask framework. It demonstrates how to manage "state" (keeping track of data over time) using **Sessions** while interacting with a user through a browser.

Here is the step-by-step breakdown of how the game works:

---

### 🏗️ 1. The Core Architecture:
This project uses a **Client-Server** model where the "state" (your score and the target number) is stored on the server using a **Session**.


* **Flask & Session:** You use `session` to remember information across different clicks or page refreshes. Without this, the game would "forget" the target number every time you submitted a guess.
* **Secret Key:** The `app.secret_key` is used to encrypt the session data so the user cannot easily cheat by looking at their browser cookies.

---

### 📂 2. Step-by-Step Logic Flow:

#### Step 1: Game Initialization:
When you first visit the page (`/`), the server checks if a game is already in progress:
* **Target Number:** It generates a random integer between 1 and 50 using `random.randint(1, 50)`.
* **Starting Score:** It gives the player a starting "life" or score of 5.
* **Initial Message:** It sets the welcome instruction: "Guess a number between 1 to 50".

#### Step 2: Processing the Guess (The POST Request):
When you type a number and hit "Submit," the browser sends a **POST** request to the server:
1.  **Retrieval:** Flask pulls the `guess` from the HTML form and retrieves the `number` and `score` from the session memory.
2.  **Validation:** It checks if the guess is within the valid 1–50 range.
3.  **Comparison Logic:**
    * If the guess is **too high**, it tells you to try lower.
    * If the guess is **too low**, it tells you to try higher.
    * If the guess matches the **target number**, you get a "Congratulations" message.
4.  **Score Reduction:** Every time you guess, the server subtracts 1 from your score.

#### Step 3: Game Over or Win:
The server constantly monitors the `score`.If the score hits 0 and you haven't guessed the number, the message updates to "Game Over! You Lost".

#### Step 4: Resetting the Game:
The `/reset` route is a simple utility that clears the session memory. This deletes the current target number and score, forcing the main page to generate a brand-new game when you visit it again.

---

### 🔄 3. Data Flow Diagram:
This diagram shows how the information travels from your brain to the computer's memory.


1.  **Input:** You enter a guess in the HTML `index.html` template.
2.  **Check:** Flask compares your input against the number stored in the `session`.
3.  **Update:** The `message` and `score` are updated in the session.
4.  **Output:** The page reloads, and the new message and score are displayed back to you.


# Output(Number Guessing Game):

1)<img width="1920" height="1021" alt="Screenshot (159)" src="https://github.com/user-attachments/assets/af37e638-7808-402c-8718-e83dc1389832" />

2)<img width="1920" height="1017" alt="Screenshot (160)" src="https://github.com/user-attachments/assets/4682bdb0-ad0a-4dba-9567-4c33c4e3df81" />

3)<img width="1920" height="1024" alt="Screenshot (161)" src="https://github.com/user-attachments/assets/d64e02ab-1f92-48b8-bcf8-8cabf83c4104" />

4)<img width="1920" height="1014" alt="Screenshot (162)" src="https://github.com/user-attachments/assets/850d8085-20a9-42be-9b81-c8f8ec53656a" />
