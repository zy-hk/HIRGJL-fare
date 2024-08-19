Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        'This program substitues English letters for letters in the baconian alphabet.

        Dim alphabet() As String
        Dim bacon_alphabet() As String
        Dim ciphertext As String = ""
        Dim plaintext As String

        'Sets alphabet and morse alphabet (indexes for each letter are the same)
        alphabet = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}
        bacon_alphabet = {"AAAAA", "AAAAB", "AAABA", "AAABB", "AABAA", "AABAB", "AABBA", "AABBB", "ABAAA", "ABAAA", "ABAAB", "ABABA", "ABABB", "ABBAA", "ABBAB", "ABBBA", "ABBBB", "BAAAA", "BAAAB", "BAABA", "BAABB", "BAABB", "BABAA", "BABAB", "BABBA", "BABBB"}


        plaintext = InputBox("Enter your text to be encrypted")
        plaintext = UCase(plaintext)

        'Fixed loop repeating for each letter to be encrypted
        For counter = 0 To Len(plaintext) - 1
            'Fixed loop for each letter in the alphabet (Matching plaintext to the alphabet) (0 to 26 - 1)
            For count = 0 To 25
                'If the letter of plaintext is that letter of the alphabet, then take the bacon letter at the same index
                If plaintext(counter) = alphabet(count) Then
                    ciphertext = ciphertext & bacon_alphabet(count) & " "
                End If
            Next
        Next

        RichTextBox1.Text = ciphertext
    End Sub
End Class
