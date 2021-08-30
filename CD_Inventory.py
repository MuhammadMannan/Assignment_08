#------------------------------------------#
# Title:  CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Muhammad Mannan 20201-Jan-27 modefied file
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.dat'
lstOfCDObjects = []
import pickle

class CD:
    """Stores data about a CD:
    
    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    def __init__(self, cd_id, cd_title, cd_artist):
        self.cdid = cd_id
        self.cdtitle = cd_title
        self.cdartist = cd_artist
    
    def cd_id(self):
        return self.cd_id
    
    def cd_title(self):
        return self.cd_title
    
    def cd_artist(self):
        return self.cd_artist

    def __str__(self):
        return(str(self.cdid) + ', ' + self.cdtitle + ' by: ' + self.cdartist)

    def removeCD(cdNumber, cdList):
        
        """Function that is utilized to delete and entry from the inventory or
        an element from the list containing dictionaries. The value/entry number
        the user enters is used to search in the dictionary containing the key
        and value the user has entered and then deletes that element from the 2d table (lstTbl).
        Args:
            cdNumber (integer): an integer value is entered which corresponds to the entry number for the cd the
            user would to remove from inventory
            cdList (list containing dictionaries): 2D table of date (or a list of dictionaries)
            which contains the data in memory during the time the program is running.

        Returns:
            None.
        """
        intRowNr = -1
        for row in cdList:
            try:
                intRowNr += 1
                tmp=vars(row)
                checknum=tmp.get("_CD__cd_id")
                if checknum == (cdNumber):
                    del cdList[intRowNr]
                    return True
                else:
                    ('Please pick a valid entry to remove')
            except UnboundLocalError:
                print("Please pick a valid entry to remove")  

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """

    def load_inventory(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries
        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.
        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'rb')
        pcklFile = pickle.load(objFile)
        for line in pcklFile:
            table.append(line)
        objFile.close()

    def save_inventory(file_name, table):
        """Function to write data in lstTbl to a .dat file

        Writes the data from a 2D table (lstTbl) into a data file file_name
        (list of dicts) table one line in the file represents one dictionary row in table.
        Args:
            file_name (string): file name which is used to write data to
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        Returns:
            None.
        """
        objFile = open(file_name, 'wb+')
        pickle.dump(table, objFile)
        objFile.close()
    pass

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    def display_menu():
        """Displays a menu of choices to the user.
        Args:
            None.
        Returns:
            None.
        """
        print(
            'Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')
    
    def user_choice():
        """Gets user input for menu selection.
        Args:
            None.
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input(
                'Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
   
    def showInventory(myTbl):
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in myTbl:
            print(row)
        print('======================================')
    
    def cdInfo():
        while True:
            try:
                strID = int(input('Enter ID: ').strip())
                break
            except ValueError:
                print('Please enter a number!')
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        cdObj=CD(strID, strTitle, strArtist)
        return cdObj
    pass

    def removalInfo():
            """Asks user to input the CD ID to determine which entry to remove from inventory currently in memory.
            Returns:
                Int: entry (integer) number. 
            """
            while True:
                try:
                    intIDDel = int(input('Which ID would you like to delete? ').strip())
                    break
                except ValueError:
                    print('Please enter an ID number')
            return intIDDel

# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
try:
    FileIO.load_inventory(strFileName, lstOfCDObjects)
except FileNotFoundError:  # the file is created if it doesn't already exist
    FileIO.save_inventory(strFileName, lstOfCDObjects)

# Display menu to user
while True:
    IO.display_menu()
    userchoice=IO.user_choice()
        # show user current inventory
    
    if userchoice.lower()=='i':
        IO.showInventory(lstOfCDObjects)
        pass
        
        # let user add data to the inventory
    elif userchoice.lower()=='a':
        newCD = IO.cdInfo()
        lstOfCDObjects.append(newCD) 
        IO.showInventory(lstOfCDObjects)       
        pass
        
        # let user save inventory to file
    elif userchoice.lower()=='d':
        IO.showInventory(lstOfCDObjects)
        # 3.5.1.2 ask user which ID to remove
        cdNumber = IO.removalInfo()
        # 3.5.2 search thru table and delete CD
        removedCD = CD.removeCD(cdNumber, lstOfCDObjects)
        if removedCD:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        IO.showInventory(lstOfCDObjects)
    
    elif userchoice.lower()=='s':
        IO.showInventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input(
                'The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue
        
        # let user load inventory from file
    elif userchoice.lower()=='l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input(
            'type \'yes\' to continue and reload from file. otherwise reload will be canceled ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.showInventory(lstOfCDObjects)
        else:
            input(
                'canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.showInventory(lstOfCDObjects)
        continue

        # let user exit program
    elif userchoice.lower()=='x':
        break