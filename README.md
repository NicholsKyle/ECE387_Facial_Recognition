# ECE387_Facial_Recognition

**Version 1.2.1**

This repository includes detailed information about a facial recognition system using the PYNQ-Z1 board. For this project, two indipendent projects are working in conjuction:

1. Web Scrapping    
We are obtaining the name and profile picture of each member of a private Facebook group. Those profile pictures are then saved, the name being the name on the Facebook page, into a file to be read later. 

2. Facial Recognition    
The images saved by the web scraper are read into the facial recognition system. The system then compares the saved image to the live video feed from the webcam. The system will then output the live feed to a computer monitor. The displayed feed will show a box around earch persons face, if the person is recognized by the system that persons name will appear under the box. If the person is not recognized, the word "unknown" will appear under the box. "Unknown" simply means that the person is not a member of the Facebook group.

---

### Getting Started

1. PYNQ-Z1 Board
   * To connect the PYNQ board to your computer, use this [guide](http://pynq.readthedocs.io/en/v2.0/getting_started.html).

2. Web Scrapping 

3. Facial Recognition 
   * In order to use the facial recongination libary, you must first download the libary to the PYNQ board. The board must have access to the internet for this download. See the PYNQ guide above for details on connecting your board to the internet.
   * **!!! THIS DOWNLOAD WILL TAKE 5+ HOURS !!!**
   * Instructions to download the libary are [here](https://github.com/IarveJ/PYNQ_facialRec#installation). 
