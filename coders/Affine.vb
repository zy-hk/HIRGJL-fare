Imports System.Runtime.CompilerServices
Imports System.Runtime.Serialization
Imports System.Security.Cryptography.Pkcs

Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        'Declare variables
        Dim key_A As Integer
        Dim key_B As Integer
        Dim text As String
        Dim letter As Integer
        Dim ciphertext As String = ""

        'gets inputs from user
        text = InputBox("Enter text to be encrypted. no spaces, no non-letter characters")
        key_A = InputBox("Enter key A (in C = AX + B) must be 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, or 25")
        'validates key_A, as it must be one of below numbers
        While key_A <> 1 And key_A <> 3 And key_A <> 5 And key_A <> 7 And key_A <> 9 And key_A <> 11 And key_A <> 15 And key_A <> 17 And key_A <> 19 And key_A <> 21 And key_A <> 23 And key_A <> 25
            MsgBox("Invalid, key A must be 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, or 25")
            key_A = InputBox("PLease re-enter key A, must be 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, or 25")
        End While
        key_B = InputBox("Enter key B (a number) (in C = AX + B)")


        'sets text to uppercase (so that the ascii stuff works)
        text = UCase(text)

        'fixed loop repeating for every letter
        For counter = 0 To Len(text) - 1
            'takes a letter fromm the text, then converts it to ascii. Takes 64 away, so that is is between 1 and 26. Uses usual affine cipher equation (C = AX + B)
            letter = ((Asc(text(counter)) - 65) * key_A) + key_B
            'Modulo, makes sure it is a letter in the alphabet.
            While letter >= 26
                letter = letter - 26
            End While
            'adds letter to the encrypted text
            ciphertext = ciphertext & Chr(letter + 65)
        Next

        'displays ciphertext
        RichTextBox1.Text = ciphertext
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        Dim key_A As Integer
        Dim key_B As Integer
        Dim ciphertext As String
        Dim plaintext As String = ""
        Dim asc_letter As Integer
        Dim letter As Single

        'Gets ciphertext from user and uppercases it
        ciphertext = InputBox("Please enter the ciphertext to be decrypted (No spaces, no non letter characters)")
        ciphertext = UCase(ciphertext)

        key_A = InputBox("Enter key A (in Y = AX + B) must be 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, or 25")
        'validates key_A, as it must be one of below numbers
        While key_A <> 1 And key_A <> 3 And key_A <> 5 And key_A <> 7 And key_A <> 9 And key_A <> 11 And key_A <> 15 And key_A <> 17 And key_A <> 19 And key_A <> 21 And key_A <> 23 And key_A <> 25
            MsgBox("Invalid, key A must be 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, or 25")
            key_A = InputBox("PLease re-enter key A, must be 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, or 25")
        End While

        key_B = InputBox("Enter key B (a number) (in Y = AX + B)")

        For counter = 0 To Len(ciphertext) - 1
            'Applies a rearranged Y = AX + B onto an individual letter to decode
            asc_letter = ((Asc(ciphertext(counter)) - 65) - key_B)
            'Makes sure letter is not negative
            While asc_letter < 0
                asc_letter = asc_letter + 26
            End While
            'remaining part of the equation
            letter = asc_letter / key_A
            'letter may not equal a whole number (and so not a letter), so conditional loop adds 26 until letter will equal a whole number
            While letter <> Int(letter)
                asc_letter = asc_letter + 26
                letter = asc_letter / key_A
            End While
            'Turns letter from Ascii to a letter and adds it to plaintext
            plaintext = plaintext & Chr(letter + 65)
        Next

        'displays plaintext
        RichTextBox2.Text = plaintext
    End Sub

    Private Sub RichTextBox1_TextChanged(sender As Object, e As EventArgs) Handles RichTextBox1.TextChanged

    End Sub
End Class
