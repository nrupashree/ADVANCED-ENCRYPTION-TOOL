# ADVANCED ENCRYPTION TOOL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: N RUPA SHREE

*INTER ID*: CTIS6532

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING 

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

DESCRIPTION:
  The Advanced Encryption Tool is a cybersecurity-based application developed to ensure the confidentiality and security of sensitive data by using strong cryptographic techniques. In today’s digital world, data security has become a major concern due to increasing cyber threats such as hacking, data breaches, and unauthorized access. This project aims to provide a reliable solution for protecting files through encryption and decryption using the Advanced Encryption Standard (AES-256), which is one of the most secure encryption algorithms widely used across industries.

AES-256 is a symmetric key encryption algorithm that uses a 256-bit key length to convert plain data into an unreadable format called ciphertext. Only users who possess the correct password or key can decrypt the data back to its original form. This ensures that even if the file is accessed by unauthorized users, the content remains protected. The application enhances security further by using key derivation techniques such as PBKDF2 (Password-Based Key Derivation Function 2), which strengthens the password by applying hashing and multiple iterations, making it resistant to brute-force attacks.

The tool is designed with a user-friendly interface, allowing users to easily select files and perform encryption or decryption operations. During encryption, the system generates a random salt and initialization vector (IV), which are combined with the encrypted data and stored in the output file. This ensures that even if the same file is encrypted multiple times with the same password, the output will be different each time, increasing security. The encrypted file is saved with an extension such as “.enc”, indicating that it is protected.

For decryption, the application reads the encrypted file, extracts the salt and IV, and regenerates the encryption key using the user-provided password. If the password is correct, the file is successfully decrypted and restored to its original format. If an incorrect password is entered, the process fails, thereby preventing unauthorized access.

One of the major advantages of this tool is its simplicity combined with strong security. It can be used by individuals as well as organizations to protect confidential documents, personal files, or sensitive business data. Additionally, the tool can be extended by integrating a graphical user interface (GUI), adding features like file selection dialogs, password strength indicators, and progress bars to enhance usability.

In conclusion, the Advanced Encryption Tool demonstrates the practical implementation of cryptography in real-world applications. It highlights the importance of data protection and provides a secure and efficient method for file encryption and decryption. This project not only strengthens understanding of encryption algorithms but also contributes to building secure software systems in the field of cybersecurity.


OUTPUT:
🔐 Advanced Encryption Tool (AES-256)
1. Encrypt File
2. Decrypt File
3. Exit
Enter choice: 1
Enter file path: test.txt
Enter password: Abc@1234
✅ File encrypted successfully: test.txt.enc

🔐 Advanced Encryption Tool (AES-256)
1. Encrypt File
2. Decrypt File
3. Exit
Enter choice: 2
Enter encrypted file path: test.txt.enc
Enter password: Abc@1234
✅ File decrypted successfully: test.txt_decrypted
