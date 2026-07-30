import customtkinter as ctk

from calculator import Calculator
import theme


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class CalculatorApp:

    def __init__(self, root):

        self.root = root
        self.root.title("iPhone Calculator")
        self.root.geometry("350x650")
        self.root.resizable(False, False)

        self.root.configure(
            fg_color=theme.WINDOW_BG
        )

        self.calculator = Calculator()


        # Display
        self.display = ctk.CTkEntry(
            root,
            font=("Segoe UI", 35),
            justify="right",
            text_color="white",
            fg_color="black",
            height=80,
            border_width=0
        )

        self.display.pack(
            fill="both",
            padx=15,
            pady=20,
            ipady=10
        )

        self.display.insert(0, "0")


        # Button Frame
        self.button_frame = ctk.CTkFrame(
            root,
            fg_color=theme.WINDOW_BG
        )

        self.button_frame.pack(
            expand=True,
            fill="both",
            padx=15,
            pady=15
        )


        self.create_buttons()



    def create_buttons(self):

        buttons = [
            ["AC", "←", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]


        for row_index, row in enumerate(buttons):

            for col_index, button in enumerate(row):


                # Function buttons
                if button in ["AC", "←", "%"]:
                    text_color = "black"
                    font_style = ("Segoe UI", 18)

                # Operator buttons
                elif button in ["/", "*", "-", "+", "="]:
                    text_color = "white"
                    font_style = ("Segoe UI", 25)

                # Number buttons
                else:
                    text_color = "white"
                    font_style = ("Segoe UI", 25)



                btn = ctk.CTkButton(
                    self.button_frame,
                    text=button,
                    font=("Segoe UI",22),
                    text_color=text_color,
                    corner_radius=50,
                    height=40,
                    fg_color=self.get_color(button),
                    hover_color="#666666",
                    command=lambda b=button: self.button_click(b)
                )


                # Special layout for last row
                if button == "0":
                    btn.grid(
        row=row_index,
        column=0,
        columnspan=2,   # 0 button takes two columns
        padx=5,
        pady=5,
        sticky="nsew"
    )

                elif button == ".":
                     btn.grid(
        row=row_index,
        column=2,
        padx=5,
        pady=5,
        sticky="nsew"
    )

                elif button == "=":
                    btn.grid(
        row=row_index,
        column=3,
        padx=5,
        pady=5,
        sticky="nsew"
    )

                else:
                   btn.grid(
        row=row_index,
        column=col_index,
        padx=5,
        pady=5,
        sticky="nsew"
    )


        for i in range(4):

            self.button_frame.grid_columnconfigure(
                i,
                weight=1
            )


        for i in range(5):

            self.button_frame.grid_rowconfigure(
                i,
                minsize=70
            )




    def get_color(self, button):

        if button in ["/", "*", "-", "+", "="]:

            return theme.OPERATOR_BUTTON


        elif button in ["AC", "←", "%"]:

            return theme.FUNCTION_BUTTON


        else:

            return theme.NUMBER_BUTTON




    def button_click(self, button):

        if button == "AC":

            result = self.calculator.clear()


        elif button == "←":

            result = self.calculator.backspace()


        elif button == "=":

            result = self.calculator.calculate()


        elif button == "%":

            result = self.calculator.percentage()


        elif button == "*":

            result = self.calculator.add_input("*")


        elif button == "/":

            result = self.calculator.add_input("/")


        else:

            result = self.calculator.add_input(button)



        self.display.delete(
            0,
            "end"
        )

        self.display.insert(
            0,
            result)




if __name__ == "__main__":

    root = ctk.CTk()

    app = CalculatorApp(root)

    root.mainloop()