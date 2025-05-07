# Affine-Cypher
This was an implementation of a topic in a lab of Information, Storage and Management Course, the Topic was Affine Encryption and Decryption, so I simplify the method, and made a python code that take the input from the user in form of (Plain/Cypher Text, Two-part Encryption/Decryption Keys, the process choice) &amp; return the chosen operation output.

## What I Did
1. Used ``alpha`` and ``beta`` dictionaries to store the alphabet to index and vise-versa.
2. Created ``modular_inverse`` function that takes 3 parameters: ``(m, mod, j)``, where ``m`` is the first part of the key, ``mod`` is the variable that have 26 stored in it to represent the modules parameter, and ``j`` to keep track of ``mod`` relatively to modular inverse of ``m``.
3. Created both ``daffine`` and ``eaffine`` for decrypting and encrypting respectfully, while ``daffine`` taking the returned value of ``modular_inverse`` stored in ``min`` variable, and ``eaffine`` taking ``m`` for the sake of the encryption process, while both of them taking ``k`` and ``p``, for the second part of the key, and the plain/cipher text.
4. Created the ``affine`` function that initialize the inputs and check for the operation that will be operating, and keep the user from choosing an invalid operation, and execute the whole program.
