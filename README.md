# DataCampAutoGUI
GUI Automation for DataCamp's learning modules

IMPORTANT:
When using the .py file for the first time, be sure to change 'PictureDirectory' to a raw string containing the location of the folder. 
(e.g., r'C:\Users\yourname\Desktop\Folder\Subfolder\PictureDirectory')

If you're experiencing any trouble with OpenCV locating the images on your screen, try setting ConfidenceInterval to a lower value (between 0 and 1). Of course, if your screen is a significantly different resolution from the one where the screenshots were taken, you may need to overwrite the files in the PictureDirectory folder with snipped images of your own screen. 

To emergency cancel the GUI Automation, drag the cursor to one of the corners of the screen.

DESCRIPTION:
This script automates the process of working through a DataCamp learning module. It locates buttons of interest on screen and responds to them appropriately. However, if your goal is to accrue points during the modules, this program likely won't suffice. It only gets points for watching the videos and answering multiple choice questions.

Issues:
Currently, the program's ability to answer multiple-choice questions is limited: it often gets stuck in an endless loop.
