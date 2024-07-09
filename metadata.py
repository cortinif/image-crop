# Version info from Google Chrome
# Get this info with util `pyi-grab_version`

# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
    # filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
    # Set not needed items to zero 0.
    filevers=(78, 0, 3904, 108),
    prodvers=(78, 0, 3904, 108),
    # Contains a bitmask that specifies the valid bits 'flags'r
    mask=0x17,
    # Contains a bitmask that specifies the Boolean attributes of the file.
    flags=0x0,
    # The operating system for which this file was designed.
    # 0x4 - NT and there is no need to change it.
    OS=0x4,
    # The general type of file.
    # 0x1 - the file is an application.
    fileType=0x1,
    # The function of the file.
    # 0x0 - the function is not defined for this fileType
    subtype=0x0,
    # Creation date and time stamp.
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904b0',
        [StringStruct(u'CompanyName', u'Smart Tech Comapny Ldt'),
        StringStruct(u'FileDescription', u'Image Crop'),
        StringStruct(u'FileVersion', u'1, 0, 0'),
        StringStruct(u'InternalName', u'image_crop_exe'),
        StringStruct(u'LegalCopyright', u'Copyright 2024 STS. All rights reserved.'),
        StringStruct(u'OriginalFilename', u'image_crop.exe'),
        StringStruct(u'ProductName', u'image_crop'),
        StringStruct(u'ProductVersion', u'1.0.0'),
        StringStruct(u'CompanyShortName', u'STS'),
        StringStruct(u'ProductShortName', u'ic'),
        StringStruct(u'LastChange', u'ND'),
        StringStruct(u'Official Build', u'1')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)