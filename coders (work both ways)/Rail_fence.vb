Imports System.Net.Http

Public Class Form1
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        'Declares variables
        Dim text As String
        Dim num_parts As Integer
        Dim num_rails As Integer
        'Declares more variables (the rails)
        Dim rail1 As String = ""
        Dim rail2 As String = ""
        Dim rail3 As String = ""
        Dim rail4 As String = ""
        Dim rail5 As String = ""

        'Gets text from user
        text = InputBox("Please enter text. Visible characters only, NO SPACES")

        'Asks for number of rails (3-5)
        num_rails = InputBox("Please enter the number of rails (MUST BE BETWEEN 3 AND 5")

        'Calculates the number of parts (the number of times it goes 1232 etc.)
        num_parts = (num_rails - 1) * 2

        'While loop adding "X"s so that the text length is divisible by the number of parts
        While Len(text) / num_parts <> Int(Len(text) / num_parts)
            text = text & "X"
        End While

        'Loop repeating for every letter in the text assigning letters to rails
        For counter = 0 To Len(text) - 1
            'Assigns rail 1, 2, and 3
            rail1 = rail1 & text(counter)
            rail2 = rail2 & text(counter + 1)
            rail3 = rail3 & text(counter + 2)
            'If/else if for 4&5 rails
            If num_rails = 4 Then
                rail4 = rail4 & text(counter + 3)
                rail3 = rail3 & text(counter + 4)
            ElseIf num_rails = 5 Then
                rail4 = rail4 & text(counter + 3)
                rail5 = rail5 & text(counter + 4)
                rail4 = rail4 & text(counter + 5)
                rail3 = rail3 & text(counter + 6)
            End If
            'Adds the final letter onto rail 2, regardless of the number of rails
            rail2 = rail2 & text(counter + (num_parts - 1))
            'Adds a certain number to counter depeending on the number of rails
            counter = counter + num_rails + (num_rails - 3)
        Next

        'Displays Plaintext
        RichTextBox2.Text = (rail1 & " " & rail2 & " " & rail3 & " " & rail4 & " " & rail5)

    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        Dim text1 As String
        Dim text2 As String
        Dim text3 As String
        Dim text4 As String
        Dim text5 As String
        Dim n As Integer
        Dim num_rails As Integer
        Dim ciphertext As String = ""

        num_rails = InputBox("Enter number Of rails (3-5)")

        text1 = InputBox("Enter text on rail 1")
        text2 = InputBox("Enter text on rail 2")
        text3 = InputBox("Enter text on rail 3")

        If num_rails = 4 Then
            text4 = InputBox("Enter text on rail 4")
        ElseIf num_rails = 5 Then
            text4 = InputBox("Enter text on rail 4")
            text5 = InputBox("Enter text on rail 5")
        End If



        n = 0

        For counter = 0 To Len(text1) - 1
            ciphertext = ciphertext & text1(counter)
            ciphertext = ciphertext & text2(counter * 2)
            ciphertext = ciphertext & text3(counter + n)

            If num_rails = 4 Then
                ciphertext = ciphertext & text4(counter)
                ciphertext = ciphertext & text3(counter * 2 + 1)

            ElseIf num_rails = 5 Then
                ciphertext = ciphertext & text4(counter * 2)
                ciphertext = ciphertext & text5(counter)
                ciphertext = ciphertext & text4(counter * 2 + 1)
                ciphertext = ciphertext & text3(counter * 2 + 1)
                'n = n + 1

            Else
                n = n - 1
            End If

            ciphertext = ciphertext & text2(counter * 2 + 1)
            n += 1
        Next

        RichTextBox1.Text = ciphertext
    End Sub

    Private Sub RichTextBox1_TextChanged(sender As Object, e As EventArgs) Handles RichTextBox1.TextChanged

    End Sub
End Class
