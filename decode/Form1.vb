Public Class Form1
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Dim square(,) As String
        Dim text As String
        Dim across As String
        Dim down As String
        Dim letters As String
        Dim plaintext As String = ""

        'Gets ciphertext from user
        text = InputBox(“Please enter your ciphertext (WITHOUT SPACES.)”)

        'Fills 2D array (polybius square)
        square = {{" ", " ", " ", " ", " ", " "},
                    {" ", "A", "B", "C", "D", "E"},
                    {" ", "F", "G", "H", "I", "K"},
                    {" ", "L", "M", "N", "O", "P"},
                    {" ", "Q", "R", "S", "T", "U"},
                    {" ", "V", "W", "X", "Y", "Z"}}

        'Fixed loop finding across and down from ciphertext, finding the letter on the grid, and adding the letter to plaintext 

        For counter = 0 To Len(text) - 1
            across = text(counter)
            down = text(counter + 1)
            'MsgBox(down & ", " & across)
            plaintext = plaintext & square(down, across)
            counter = counter + 1
        Next

        'Makes a box with the plaintext      
        RichTextBox1.text = plaintext
    End Sub

    Private Sub RichTextBox1_TextChanged(sender As Object, e As EventArgs) Handles RichTextBox1.TextChanged

    End Sub
End Class
