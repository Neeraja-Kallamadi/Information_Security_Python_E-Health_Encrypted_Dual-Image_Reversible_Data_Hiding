# ENCRYPTED DUAL-IMAGE REVERSIBLE DATA HIDING TO SECURE PATIENT INFORMATION IN E-HEALTHCARE

This project represents a cutting-edge fusion of information security principles, leveraging cryptographic measures and steganographic methods, to fortify the protection of patient data within the e-healthcare landscape.

GRAYSCALE IMAGE: A grayscale image is an image composed of varying shades of gray, typically represented using 8 bits per pixel, where each pixel's intensity value represents a specific shade of gray, ranging from black to white.

DICOM IMAGE: A DICOM image is a medical imaging format often employing 16 bits per pixel and adhering to the Digital Imaging and Communications in Medicine (DICOM) standard, designed for the storage and exchange of medical images and related patient information.

PAILLIER CRYPTOSYSTEM:
The Paillier cryptosystem is a public-key cryptosystem that allows for the secure encryption of data. It is primarily known for its homomorphic properties, which enable mathematical operations on encrypted data without the need for decryption, making it useful for privacy-preserving computations and secure data storage. Paillier cryptosystem is widely used in various cryptographic applications, including secure multi-party computation and encrypted data aggregation.

DATA EMBEDDING: Initially, a 512x512 8-bit grayscale or 16-bit DICOM image serves as the cover image, which is then divided into two parts, coverimage1 and coverimage2. Each coverimage undergoes encryption using the Paillier cryptosystem. The patient information is treated as a confidential message, and zone values are computed following a specific algorithm. Subsequently, reduced secret and zone values are derived to prevent image distortion from an excessively large secret message. Both reduced secret and zone values are then encrypted using the Paillier cryptosystem. These encrypted reduced values are embedded in encrypted coverimage1 and encrypted coverimage2 to create stegoimage1 and stegoimage2, respectively, thereby forming a stego image.

DATA EXTRACTION AND IMAGE RECOVERY PHASE: In the data extraction and image recovery phase, stegoimage1 and stegoimage2 are decrypted using the Paillier cryptosystem to successfully recover the original cover image and the confidential secret image.

WATERMARK AUTHENTICATION: Furthermore, to ensure data integrity and authentication, an additional step involves embedding an 8-bit grayscale watermark image of size 256x256 pixels into the data during the embedding phase, utilizing the Alpha-Blending technique. This watermark image serves as a unique identifier. During data extraction and the image recovery phase, a Watermark Detection technique is employed to extract the watermark from the stego image and compare it to a reference image. If both watermark images match, it confirms the authenticity and integrity of the data; otherwise, any discrepancies indicate that unauthorized modifications have been made.

In this comprehensive approach, encrypted dual image reversible data hiding is employed using 512x512 grayscale or DICOM images, supplemented by watermark authentication. This integrated strategy not only enhances the security of patient information within the realm of e-healthcare but also ensures both confidentiality and data integrity, providing a robust and reliable solution.

STATISTICAL METRICS: To thoroughly evaluate the performance of this specified algorithm, a range of metrics is employed, including Peak Signal-to-Noise Ratio (PSNR), Mean Square Error (MSE), Structural Similarity Index Matrix (SSIM), Normalized Absolute Error (NAE), Normalized Cross-correlation (NCC), Embedding Rate (bpp) and BER (Bit Error Rate). These metrics collectively provide insights into the algorithm's efficiency in terms of image quality, data preservation, and capacity.

HISTOGRAM ANALYSIS: Histogram analysis is conducted for both the cover image and the stego image. A histogram is a visual representation of pixel intensity distribution within an image. Attackers often employ histogram analysis to gain insights into embedded information, comparing histograms of the cover and stego images. The robustness of a data hiding method is determined by the degree of similarity between corresponding histograms, with closer resemblance indicating higher resistance to such attacks. This analysis provides valuable information regarding the algorithm's ability to conceal data effectively while maintaining the integrity of the image.

# OVERVIEW:
![overview](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/2ef3c795-9b8b-498b-b6e1-76fd142e443a)

![test_images](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/e0ad5d42-6bad-49a9-9653-9957551b1d10)

![performance_metrics](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/37b01427-6da9-416a-b16c-dd2ecc0fb7f6)

# PAILLIER CRYPTOSYSTEM ALGORITHM
![paillier1](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/38b6e2f1-83d9-464b-beee-058c4cb1162e)
![paillier2](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/a91dbe5a-e359-4b92-8a55-c4bce5974ee3)
![paillier3](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/f46b8555-f7c4-4251-b774-2ecb49f67141)

# DATA EMBEDDING ALGORITHM
![data_embedding1](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/6afb42f8-5e16-4c25-8e23-2f5c46ee5c4f)
![data_embedding2](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/6207c4f7-9280-4d5c-baf8-cc473c29362e)
![data_embedding3](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/59e5c76c-3770-4ec8-ab21-7fab2090aa90)
![data_embedding4](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/2ea11993-297d-4566-b825-68dd6946a8e4)
![data_embedding5](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/85c52106-fc32-4138-9f2d-116731ed854f)
![data_embedding6](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/9f422705-5326-49e5-bc88-5c7055b0e36c)

# DATA EXTRACTION AND IMAGE RECOVERY ALGORITHM
![data_extraction_image_recovery1](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/ba0a741a-6ebb-4f93-9766-71ebe9a83c15)
![data_extraction_image_recovery2](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/1a4b823c-a976-431e-b8f5-8e06c21ef9f9)

