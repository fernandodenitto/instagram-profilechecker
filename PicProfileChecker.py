from PIL import Image
import requests
from io import BytesIO


def emptyPicProfileFromURL(picProfileURL):

    """ Check if the URL of the Profile Pic contains the substring 
        "44884218_345707102882519_2446069589734326272_n.jpg" that is
        the name of the file that Instagram use for the emplty photo profile.
        The function returns true if the Profile Picture is not present, false otherwise.
    """

    emptyPicURL="44884218_345707102882519_2446069589734326272_n.jpg"

    return (emptyPicURL in picProfileURL)


#FOR TEST
#print(checkPicProfileFromURL("URL TO TEST"))


# THE FOLLOWING FUNCTIONS COULD BE USE IN THE FUTURE 
# IF INSTAGRAM WILL DECIDE TO CHANGE THE URL OF THE 
# STANDARD PROFILE EMPTY PICTURE. IF THIS WILL HAPPEN
# IT WILL BE NECESSARY TO COMPARE THE PROFILE PICTURE
# WITH THE EMPTY ONE SAVED IN THE DIRECTORY /img IN
# THIS REPOSITORY

def imageDiff(image1path,image2path):
    """
    This function return the difference in term of percentage of RGB between two images.
    Images have to be of the same size and same kind (e.g.JPEG).
    Equals image have to return 0!
    Inputs are the path of the images
    """
    
    i1 = Image.open(image1path)
    i2 = Image.open(image2path)
    assert i1.mode == i2.mode, "Different kinds of images."
    #assert i1.size == i2.size, "Different sizes."
    
    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
    
    ncomponents = i1.size[0] * i1.size[1] * 3
    return (dif / 255.0 * 100) / ncomponents #Difference in percentage


def imageDiffURL(image1url,image2url):
    """
    This function return the difference in term of percentage of RGB between two images.
    Images have to be of the same size and same kind (e.g.JPEG).
    Equals image have to return 0!
    Inputs are the URL of the two images
    """

    #Retrieve Image 1 from URL
    response1 = requests.get(image1url)
    i1 = Image.open(BytesIO(response1.content))

    #Retrieve Image 2 from URL
    response2 = requests.get(image2url)
    i2 = Image.open(BytesIO(response2.content))

    assert i1.mode == i2.mode, "Different kinds of images."
    #assert i1.size == i2.size, "Different sizes."
    
    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
    
    ncomponents = i1.size[0] * i1.size[1] * 3
    return (dif / 255.0 * 100) / ncomponents #Difference in percentage

print(imageDiffURL("https://instagram.fcdg1-1.fna.fbcdn.net/vp/bde9a32e6cadcee349b85053b36f103c/5E695BF1/t51.2885-19/44884218_345707102882519_2446069589734326272_n.jpg?_nc_ht=instagram.fcdg1-1.fna.fbcdn.net","https://scontent-mxp1-1.cdninstagram.com/vp/90ffd609ae2d97be7c37f2a964e4496e/5E666F17/t51.2885-19/s320x320/71946067_575063146631396_5911669943438409728_n.jpg?_nc_ht=scontent-mxp1-1.cdninstagram.com"))
