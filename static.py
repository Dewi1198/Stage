# xml validator file
# this validator maintains the intergrity of the xml fiwalk output
# source: https://github.com/dfxml-working-group/dfxml_schema
xsdfile = "wildfrag/.xsd/dfxml.xsd"

# this dict contains the commands that are executed on the OS
commands = {
    'lsblk_big': "sudo lsblk -Jfb -o NAME,FSTYPE,ROTA,HOTPLUG,FSSIZE,FSAVAIL,FSUSED,PARTFLAGS",
    'devsize': "sudo blockdev --getsize64 /dev/{}",
    'model': r"sudo udevadm info --query=all --name=/dev/{} | grep -zoP '(?<=ID_MODEL=).*(?=\n)'",
    'serial': r"sudo udevadm info --query=all --name=/dev/{} | grep -zoP '(?<=ID_SERIAL=).*(?=\n)'",
    'mount': "sudo mount -o ro /dev/{} {}",
    'mount_check': "sudo grep -s {} /proc/mounts",
    'owndev': "sudo df {} | awk 'NR == 2 {{print $1}}'",
    'lsblk_small': "sudo lsblk -lfbn -o NAME,FSTYPE",
    'blocksize': "sudo blockdev --getbsz /dev/{}",
    'validator': "sudo xmlstarlet val -S -s {} {}",
    'fiwalk': "sudo fiwalk -IOgz -X {} /dev/{}"}

# this dict contains the sql queries needed to communicate with the database
sql = {
    'get_last_id': "SELECT last_insert_rowid();",
    'store_system': "INSERT INTO Systems (start_run,end_run) VALUES({},{});",
    'store_device': """INSERT INTO StorageDevices (model,hwid,rotational,
        hotplug,size,system_id) VALUES('{}','{}',{},{},{},{});""",
    'store_volume': """INSERT INTO Volumes (size,fs_type,free,flags,used,
        block_size,storage_device_id) VALUES({},'{}',{},'{}',{},{},{});""",
    'store_file': """INSERT INTO Files (volume_id,extension,extension_len,
        fs_compressed,size,atime,crtime,ctime,mtime,blocks,num_blocks,
        num_gaps,sum_gaps_bytes,sum_gaps_blocks,backward,num_backward,
        fragmented,hardlink_id,resident,num_hardlink,sparse,linearconsecutive,
        fs_seq,fs_nlink, fs_inode) VALUES {};""",
    'file': """({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},
        {},{},{},{},{}),""",
    'get_instances': "SELECT start_run FROM Systems",
    'get_hardlink_id': "SELECT max(hardlink_id) FROM Files"
}

# list of known file extensions
# extensions with 3 chars or less are not included in this list
# those extensions are always accepted by the cleanData function
extensions = ("$efs", "$er $er", "00_jpg_srb", "00_jpg_srz", "00_png_srz", "1092", "123dx", "1pif", "2bp ", "2sflib", "3_dpo", "3dmf", "3dsx", "3gp2", "3gp_128x96", "3gpp", "3gpp2", "3ivx", "4dindy", "600x", "7-zip", "7z.001", "7z.002", "7z.003", "7z.004", "7z.005", "7z.006", "7z.007", "7z.008", "7z.009", "7z.010", "7z.011", "7z.012", "7z.013", "7z.014", "7z.015", "7z.016", "7z.017", "7z.018", "7z.019", "7z.020", "7z.021", "7z.023", "7z.025", "7z.027", "7z.028", "7z.029", "7z.030", "7z.031", "7z.032", "7z.033", "7z.034", "7z.035", "7z.036", "7z.037", "7z.039", "7zip", "8svx", "G723-3", "SafeText", "___fpe", "_docx", "_eml", "_ipod_control", "_pdf", "_vti_bin", "_xls", "a5wcmp", "aas+A897", "ab65", "abbu", "abcd", "abcdmr", "abicollab", "acad", "acbm", "accda", "accdb", "accdc", "accde", "accdp", "accdr", "accdt", "accdu", "accdw", "access", "accft", "accountpicture-ms", "acct", "acd-zip", "acid", "acmb", "acorn", "acrypt", "acsm", "activitydiagram", "addoc", "adef", "adex", "adicht", "adiumhtmllog", "adiumlog", "adoc", "ados", "adox", "adpr", "adsm", "adson", "adts", "adups", "aepkey", "aepx", "aes256", "aexpk", "afs3", "afzplug", "aggr", "agif", "agilekeychain", "agldei", "aglsl", "ahrp", "ahtm", "aidf", "aifc", "aiff", "aifr", "akai", "alac", "alaw", "alb3", "alb4", "alb5", "ald5", "alias", "alt3", "alt5", "alt6", "amlx", "ampl", "amsm", "amsproj", "amst", "amxd", "android", "anim", "annot", "ansi", "ansr", "antifrag", "apalbum", "apdisk", "apex", "apng", "apple", "apple_partition_map", "appledouble", "application", "appt", "appv", "appxbundle", "aprj", "arch00", "architect", "archiver", "arcinfo", "arcut", "arff", "argo", "aria", "ariax", "arpx8", "artask", "artwork", "artx", "as4a", "ascii", "ascx", "asdb", "asdvdcrtproj", "asec", "ashx", "asis", "aslquery", "asmx", "asnd", "aspx", "asrp", "assoc", "atahd", "atak", "atla", "atml", "atom", "atrac", "attf", "audionote", "aupreset", "auth", "automaticdestinations-ms", "avchd", "avery", "avif", "awbs", "awdb", "awlive", "awsec", "awss", "awwp", "azw1", "azw2", "bada", "badongo", "balance", "bamboopaper", "band", "base64", "bash_history", "bash_profile", "bbfw", "bbprojectd", "bbxt", "bcard", "bdav", "bdef", "bdmv", "bdoc", "bdt2", "bdt3", "bdtp", "beam", "bean", "bexpk", "bibtex", "big5", "bilw", "bimd", "bina", "binarycookies", "bioexcess", "bitmap", "bizdocument", "bkmk", "blend", "blob", "bmp ", "bmp24", "bmp_", "bmpenx", "bmpp", "bmpr", "bmpw", "bmtp", "bobo", "book", "bookexport", "booktemplate", "bootefisignature", "bpdx", "bpmc", "bpoly", "bpwx", "br25", "br27", "br28", "br29", "br31", "br32", "br48", "bridgesupport", "brsar", "brstm", "brush", "bsdiff", "bsdl", "bson", "btab", "btapp", "btoa", "btpc", "btree", "bufr", "bulk", "bulk-003", "burn", "burntheme", "bzabw", "bzip", "bzip2", "c-map", "c1dx", "cachedump", "cadoc", "cadrg", "calca", "cals", "camelsounds", "camm", "camproj", "camrec", "camthtr", "camv", "caps", "capt", "carb", "cascii", "catdrawing", "catpart", "catproduct", "cats", "cavs", "ccitt", "ccrf", "cdda", "cddz", "cdem", "cdev", "cdfs", "cdml", "cdmm", "cdmt", "cdmtz", "cdmz", "cdoc", "cdr3", "cdr4", "cdr5", "cdr6", "cdrw", "cdrzip", "celp", "celtx", "cert", "cfml", "cfog", "cgmap", "changedb", "changedb-journal", "charset", "chml", "chord", "chtml", "chunk001", "cidb", "cimg", "cine", "cipo", "cl2lyt", "cl2tpl", "clarify", "class", "clbx", "clgx", "clip", "clipping", "clix", "clkd", "clpi", "clprj", "cm0013", "cmmp", "cmmtpl", "cmproj", "cmrec", "cmrl", "cmyk", "cmyka", "coffee", "colorpicker", "comicdoc", "comiclife", "component", "components", "compositiontemplate", "compress", "conf", "contact", "converterx", "cook", "core", "cpbitmap", "cpdt", "cpgz", "cpio", "cpmz", "cptl", "cptx", "cpvc", "crash", "craw", "crdownload", "crec", "crev", "crmlog", "crpt", "crtr", "crtx", "crwl", "crypt", "crypt10", "crypt11", "crypt12", "crypt5", "crypt6", "crypt7", "crypt8", "crypt9", "crypted", "cryptomite", "cryptra", "csar", "csassembly", "cscpkt", "cshp", "cshtml", "csmanifest", "css1", "csvx", "ctfsys", "ctit", "ctxt", "cube", "customdestinations-ms", "cvsd", "cwdb", "cweb", "cwks", "cwms", "cwss", "cwwp", "czar", "czip", "daproj", "darc", "daschema", "dash", "dat_tureg_old", "dats", "db-journal", "db.crypt5", "db.crypt7", "db.crypt8", "db2mov", "db2p", "dbfseventsd", "dbfx", "dblib", "dbmg", "dbnx", "dbpro", "dcim", "dcmd", "dctmp", "ddif", "dectest", "default", "defaultsite", "demo", "demo4", "deproj", "desc", "design", "desklink", "desktop", "devicemanifest-ms", "devicesalt", "devpackage", "devpak", "devx", "dewf", "dfti", "dfxp", "dgdat", "dgpd", "dgrh", "dhcd", "diagcab", "diagpkg", "dicm", "dicom", "dime", "dired", "disco", "discomap", "diskdefines", "disposition-notification", "dita", "divx", "djanimations", "djmusic", "djprojects", "djvu", "dk@p", "dll_1029", "dmkit", "dmmx", "dmpatch", "dmpr", "dmptrn", "dmsa", "dmsd", "dmsd3d", "dmse", "dmskm", "dmsm", "dmss", "dmtemplate", "doc#", "doce", "docenx", "dochtml", "docl", "docm", "docmhtml", "docs", "docset", "doct", "documentrevisions-v100", "docx", "docxenx", "docxl", "docxml", "doink-gs", "dothtml", "dotm", "dotmenx", "dotx", "dotxenx", "download", "dpdoc", "dpsml", "dpx ", "drmx", "drmz", "dropbox", "drw2", "drw5", "ds_store", "dscf", "dsdb", "dsml", "dstf", "dtcp-ip", "dtshd", "dtsi", "dtsx", "dump", "dv-avi", "dvddata", "dvdmedia", "dvdproj", "dvdrip", "dvr-ms", "dvsd", "dwdoc", "dwlibrary", "dxstudio", "dxtheme", "dylib", "e2ev", "eac3", "eappx", "easmx", "ebkproj", "ebmd", "ebmp", "ecfg", "ecms", "ecmt", "ecsv", "ed2k", "edat", "eddx", "edml", "edoc", "efax", "efires", "egisenc", "egisenx", "eidi", "elastik", "elev", "elfo", "email", "emaker", "embp", "emcmf", "emcx", "emix", "emlx", "emulecollection", "enc4", "encm", "enex", "enff", "enfpack", "enlx", "enpack", "enyd", "eosat", "eossa", "epdf", "epibrw", "eprtx", "epub", "equiv", "eragesoundset", "erbsql", "escpcb", "escsch", "eseq", "eslock", "esproj", "etng", "etnt", "etrg", "etxt", "event", "evrc", "evtx", "excel", "exif", "exopc", "exportedfavorites", "ext2", "ext4", "extra", "ezpx", "eztv", "f+db", "fac ", "face", "fadein", "faff", "failurerequests", "fasta", "fb2k", "fb2k-component", "fbok", "fc14", "fcarch", "fcdt", "fcfe", "fcproject", "fcpxml", "fcxe", "fdml", "fdxt", "feed-ms", "feedsdb-ms", "ffdata", "ffivw", "ffpx", "ffs_db", "fgdump-log", "fhtml", "fido", "file", "filelock", "film", "fire", "first", "fits", "flac", "flame", "flexolibrary", "fli_", "flic", "flif", "flka", "flkb", "flkw", "flmod", "flux", "flvat", "flwa", "fmap", "fmdb", "fmk4", "fmp12", "fmp3", "fmpr", "fmpsl", "fodp", "fods", "fodt", "folder", "folder.metadata", "font", "form", "fpage", "fpenc", "fpix", "fpkg", "fpos", "fppx", "fpsml", "fpweb", "fpxml", "framework", "frdat", "frdoc", "fred", "freelist", "freeway", "freshcontact", "freshroute", "fseventsd", "fsform", "fsif", "fsim", "fspro", "fsproj", "fstab", "fstick", "ftch", "ftil", "ftlx", "ftmt", "ftmx", "ftpl", "ftvx", "ftxt", "full", "fuzz", "fweb", "fwrt", "fwtb", "fwtemplate", "fwtemplateb", "g64x", "g721", "g723", "g726", "g726-2", "g726-3", "gadget", "game", "gameproj", "gca3", "gca4", "gca4base", "gdbtable", "gdbtablx", "gdoc", "gdocx", "gdraw", "gdwx", "genbank", "geodatabase-shm", "geodatabase-wal", "geojson", "getright", "gevl", "gexf", "gfar", "gform", "gif2", "gif89a", "gif_160x120", "gifenx", "giff", "gifv", "gif~c200", "gim ", "glink", "glue", "gm81", "gmap", "gmbck", "gmod", "gnote", "gnutar", "gofin", "gpbank", "gprmc", "gprx", "grade", "grads", "graf", "graffle", "grasp", "gray", "grdnt", "greenfoot", "grey", "grft", "grib", "grob", "group", "gscript", "gsheet", "gslides", "gtable", "gtar", "gthr", "guide", "gvsp", "gzip", "h-263", "h.263", "h260", "h261", "h263", "h263+", "h264", "h265", "h2song", "ham6", "ham8", "handlebars", "hathdl", "hbc2", "hbox", "hcgs", "hcom", "hdml", "hdmov", "hdmp", "hdri", "hdru", "heic", "heif", "help", "hevc", "hhtml", "hid2", "hips", "hkdb", "hm10", "hmap", "hmxp", "hmxz", "hpfs", "hpgl", "hppcl", "hsancillary", "hsql", "hstx", "html", "html5", "htmlenx", "htmls", "htmlz", "htms", "htm~", "htri", "htz5", "huge", "hwpml", "hype", "i3pack", "ia64", "ibatemplate", "ibcd", "ibro", "icalevent", "icaltodo", "icap", "icfe", "icfm", "icma", "icml", "icmt", "ico_", "icon", "icst", "id31", "id32", "idap", "idb2", "identifier", "idml", "idrc", "idrw", "idx_dll", "iflv", "iges", "igtx", "ihtml", "ilbm", "ildoc", "ilht", "im4p", "ima4", "image", "imap", "img3", "imoviemobile", "imovieproj", "imovieproject", "imovietrailer", "imported", "imscc", "imsp", "imtx", "incp", "inct", "indb", "indd", "indn", "indt", "indx", "info", "infopathxml", "ingr", "inld", "inrs", "install_backup", "installhelper", "insx", "inta", "inuse", "ioca", "ioplist", "ipdb", "ipsw", "iptc", "ipynb", "iraf", "ircp", "irix6", "irrmesh", "irtr", "isale", "isaletemplate", "isam", "isdoc", "isdocx", "ish1", "ish3", "isma", "ismv", "ispx", "iswp", "itc2", "itld", "itls", "itmsp", "itmz", "iv-vrml", "ivex", "ivue", "iw44", "iwprj", "iwtpl", "iwzip", "izzy", "jar.pack", "jasc", "jascproject", "java", "jbig", "jbig2", "jccfg3", "jcrypt", "jfif", "jfif-tbnl", "jgwx", "jhtml", "jiff", "jlqm", "jmce", "jmck", "jmcp", "jmcr", "jmcx", "jnilib", "jnlp", "joml", "journal_info_block", "jp2_", "jpeg", "jpeg_128x96", "jpeg_160x120", "jpeg_170x220", "jpegenx", "jpegx", "jpg-large", "jpg-original", "jpg2", "jpg3", "jpg_108x192", "jpg_120х178", "jpg_128x128", "jpg_128x160", "jpg_128x96", "jpg_160x120", "jpg_160x128", "jpg_170x128", "jpg_170x220", "jpg_220x176", "jpg_240x320", "jpg_320x240", "jpg_320x320", "jpg_480x320", "jpg_512x512", "jpg_56x42", "jpg_encrypted", "jpg_t", "jpg_thumb", "jpge", "jpgenx", "jpgw", "jpgx", "jpig", "jsobj", "json", "jsonld", "jspa", "jspx", "jsxbin", "jtdc", "jtif", "kahl", "kava", "kbasic", "kdbx", "kdmp", "kexi", "kext", "key-tef", "keychain", "keynote", "kfdk", "kismac", "klip", "kmtf", "kodak", "kodu", "kpdx", "kris", "kseqs", "ktspack", "laba", "label", "laccdb", "landsat", "lang", "lansat", "lasso", "lasx", "latex", "lavs", "layoutdesigner", "ldap", "ldif", "ldmt", "leotmi", "lgpl", "lime", "link", "linux", "linx", "lisp", "list", "ljpg", "localized", "location", "lock", "lock3", "log1", "log2", "log3", "log4", "log5", "log6", "log7", "log8", "log9", "logic", "logicx", "logonxp", "loop", "love", "lpcm", "lpdf", "lproj", "lrec", "lsproj", "lthmb", "lucy", "lutx", "lwac", "lwbm", "lwtt", "lxfml", "lzma", "lzma86", "lzop", "m-jpeg", "m1pg", "m2ts", "m3u8", "ma2.mmf", "maca", "macbin", "macp", "macs", "maff", "magnet", "mail", "maildb", "mailhost", "manager", "manifest", "manu", "mapimail", "maplib", "mapx", "marc", "markdn", "markdown", "marker", "mars", "marshal", "mask", "mass", "mathml", "maud", "maxfr", "mbbk", "mbfavs", "mbfs", "mbfx", "mbox", "mbz5", "mcat", "mcbn", "mcdb", "mcdx", "mcmac", "mcpp", "mcrp", "mcsp", "mcsv", "mdbhtml", "mdbx", "mdhtml", "mdimporter", "mdle", "mdmp", "mdown", "mdtext", "mdtxt", "mdwn", "mdzip", "mediawiki", "mell", "mellel", "menc", "mepx", "meta4", "metalink", "mgdatabase", "mglr", "mglt", "mglw", "mgourmet", "mgourmet3", "mhtenx", "mhtm", "mhtml", "mhtmlenx", "midi", "miff", "migitallock", "migtable", "mime", "mindnode", "minibank", "minigsf", "miniusf", "miradi", "mitsu", "mjbooktemplate", "mjdoc", "mjp2", "mjpeg", "mjpg", "mk3d", "mkII", "mkdn", "mkext", "mkey", "mkeyb", "mkv3D", "ml20", "mlraw", "mman", "mmap", "mmas", "mmat", "mmdf", "mmip", "mmmp", "mmpr", "mmpz", "mmsw", "mobi", "modd", "moff", "mogg", "mojito", "mol2", "moml", "monitorpanel", "mono", "montage", "moov", "moss", "movie", "mozeml", "mp21", "mp2v", "mp3a", "mp3g", "mp3pro", "mp3url", "mp41", "mp4a", "mp4b", "mp4v", "mpcpl", "mpdp", "mpeg", "mpeg1", "mpeg2", "mpeg4", "mpega", "mpegps", "mpg2", "mpg3", "mpg4", "mpga", "mpgv", "mpgx", "mpkg", "mpls", "mpnt", "mpp_", "mppx", "mppz", "mpqe", "mps_", "mpsub", "mptm", "mpv2", "mpv4", "mpvf", "mpwd", "mraw", "ms-tnef", "mscx", "mscz", "msdl", "msdm", "msdvd", "mshc", "mshdb", "mshi", "msie", "msor", "msproducer", "mspx", "msqm", "msrcincident", "mswd", "msys", "mtiff", "mtkt", "mtml", "mts1", "mtxt", "muimanifest", "murl", "mus  mus", "mus10", "muse", "musx", "mv85", "mv93", "mv95", "mvdx", "mvtx", "mwand", "mwav", "mwii", "mwpd", "mwpp", "mwpr", "mxc2", "mxfd", "mxls", "mxmf", "mxml", "mydocs", "mzip", "n90ap", "nabs", "naplps", "narrative", "navionics", "navmap", "nbib", "nbkt", "nclk", "ncor", "ncorx", "ncsa", "ndpi", "ndpr", "ndrv", "neis", "netcdf", "newsloc", "nfd_audio", "nfm8", "ngloss", "ngrr", "niff", "nist", "nitf", "nkey", "nlpe", "nmap", "nmbd", "nmbtemplate", "nmea", "nmgf", "nmsv", "nokogiri", "nope", "not_terminated", "note", "notebook", "notes", "novs", "npdf", "npdt", "nppe", "nsarc", "nsconfig", "nsfe", "nsla", "nsmp", "nspe", "ntfs", "nuget", "numbers", "numbers-tef", "nupkg", "nvavi", "nwcab", "nwcp", "nwctxt", "nwdb", "nx^d", "nx__", "objf", "obml", "obml15", "obml16", "obpack", "ocdc", "ocdf", "od4-9", "odccubefile", "odif", "odt#", "oeaccount", "oedb", "ognc", "ole2", "olk14contact", "olk14dbheader", "olk14msgattach", "olproj", "olsr", "omfi", "onepkg", "ontx", "oogl", "opdownload", "opef", "openbsd", "oplc", "oplx", "opml", "opsx", "opus", "opxs", "opxt", "osax", "osinstallmessages", "otlb", "otrkey", "outlook97", "owfs", "oxps", "ozf2", "ozfx3", "p2bp", "paal", "pack", "pack.gz", "package", "pact", "page", "page.security", "pages", "pages-tef", "paint", "pamp", "pando", "pandora", "panic", "pano", "paq6", "paq7", "paq8o", "par2", "part", "part00000", "part1.exe", "part1.rar", "part10.rar", "part11.rar", "part2.rar", "part3.rar", "part4.rar", "part5.rar", "part6.rar", "part7.rar", "part8.rar", "part9.rar", "partial", "passwordwallet4", "pattern", "payload", "pbix", "pblib", "pbmb", "pbproj", "pch2", "pckgdep", "pcx_", "pcxm", "pdbx", "pdf_", "pdf_tsid", "pdfa", "pdfe", "pdfenx", "pdfl", "pdfua", "pdfvt", "pdfx", "pdfxml", "peak", "pfsx", "pgal", "pgma", "pgmb", "pgmx", "pgwx", "phar", "php3", "php4", "php5", "phps", "phtm", "phtml", "pi[1-6]", "picnc", "picon", "pict", "pict1", "pict2", "pictclipping", "pictor", "pipe", "pixar", "pixate", "pixelpaint", "pjpeg", "pjpg", "pjtf", "pkcs12", "pkey", "pkg_", "pkinfo", "pkpass", "plan", "plantuml", "plist", "plsc", "plsk", "plst", "pltx", "plugin", "ply2", "pmatrix", "pncl", "png-large", "png24", "png32", "png8", "pngt", "pngw", "pnne", "pntg", "policy", "poly", "pool", "postal", "pothtml", "potm", "potmenx", "potx", "pp7m", "ppam", "ppcx", "ppdf", "ppenc", "ppnt", "ppot", "pproj", "ppsenx", "ppsm", "ppsx", "ppsxenx", "ppt3", "ppta", "ppte", "pptenx", "ppthtml", "pptl", "pptm", "pptmhtml", "pptt", "pptv", "pptx", "pptxenx", "pptxml", "prefpane", "prel", "prjx", "prnx", "pro4", "pro4dvd", "pro5", "pro5dvd", "pro5plx", "pro5x", "profile", "proj", "project", "propdesc", "properties", "proqc", "proto", "provxml", "prproj", "prs1", "prs2", "prt1", "prt2", "prvkr", "ps16", "psafe3", "psdt", "psdx", "pseg", "psf2", "psflib", "psm1", "psmd", "psml", "psmm", "pspimage", "psppalette", "psproj", "pswx", "psxprj", "ptcop", "ptif", "ptped", "pttune", "ptxt", "pubf", "pubhtml", "pubkr", "publication", "pubmhtml", "puma", "puzz", "pwbk", "pwdef", "pworks", "pwzip", "pyxel", "pzfx", "pzip", "qbquery", "qcif", "qfilter", "qgis", "qhcp", "qhtm", "qlgenerator", "qprj", "qrmx", "qtvr", "quad", "quicktimecomponents", "quiz", "quiztemplate", "quox", "raes", "raml", "rar1", "rar5", "rarenx", "rargb", "rarx", "rast", "ratDVD", "ravi", "rawraw", "rbdf", "rbxl", "rbxm", "rcproject", "rcrec", "rcut", "rdata", "rdlx", "readme", "rec_part0", "rec_part1", "rec_part2", "rec_part3", "record", "regtrans-ms", "rels", "repatch", "report", "res11", "resource", "resp", "rest", "restorelist", "rf64", "rgb8", "rgba", "rgbn", "rgdb", "rgss2a", "rgtrack", "rhistory", "rhtml", "riff", "rimg", "ring", "riscos", "rise", "rmap", "rmvb", "roadtrip", "rockwell", "roff", "rolf", "rpgm", "rpgmvm", "rpgmvo", "rpgmvp", "rpmsg", "rptr", "rptx", "rrpa", "rsdb", "rsdf", "rsrc", "rtab", "rtdf", "rtf_", "rtfd", "rtkt", "rtmap", "rtsl", "rtsp", "rtttl", "runz", "rvid", "rwsw", "s2db", "s3db", "s4ud", "s6bn", "s8bn", "sabl", "sabs", "safe", "sai2", "saif", "sami", "sats", "saveddeck", "savedsearch", "saver", "sbig", "sbpf", "sbsc", "sbst", "sc68", "scala", "scan", "scap", "sccef", "scexe", "schd", "schdoc", "schematic", "scke", "scpt", "scptd", "scriv", "scrivx", "scs11", "scsi", "sctor", "sd2f", "sdat", "sdbn", "sdev", "sdii", "sdir", "sdlic", "sdml", "sdnf", "sdoc", "sdpx", "sdr2", "sdsk", "sdtid", "sdts", "sdwx", "sdxml", "searchindexcache", "secure", "securedownload", "sedprj", "seed", "seek", "seg1", "service", "sesx", "settingcontent-ms", "sevz", "sfark", "sfcache", "sfds", "sfil", "sflb", "sfpack", "sfvidcap", "sgml", "sgvx", "sh3d", "sha1", "sha512", "sham", "shar", "sheet", "shlb", "show", "shsh", "shtm", "shtml", "siag", "sidx", "sign", "signed", "silk", "simp", "sisx", "sit!", "sit5", "sitd", "sitemap", "sites", "sithqx", "sitx", "sixel", "sjpg", "skcard", "sld3", "sld8", "sldasm", "slddrw", "sldm", "sldprt", "slds", "sldx", "slife", "sls3", "sls4", "sls5", "sls8", "smaf", "smali", "smbp", "smclvl", "smdf", "smfmf", "smht", "smil", "smilebox", "smmx", "smpg", "smpl", "smpx", "snag", "snagitstamps", "snap", "snapfireshow", "snappy", "sndb", "sndh", "snoop", "soap", "soar", "solitairetheme8", "song", "sonic", "sosi", "soundpack", "soundscript", "spar", "sparc", "spdb", "spdesignopen", "spdesignshtm", "spdesignsitemap", "spdf", "spec", "spentry", "spiff", "spin", "spkg", "splash", "split", "spml", "spot", "sppt", "spreporter", "sprite", "sprz", "spsx", "spub", "spud", "sqfs", "sqlite", "sqlite2", "sqlite3", "sqlitedb", "srec", "srep", "ssage", "ssdl", "ssif", "ssiw", "sskd", "ssmssqlproj", "steamstart", "stem", "stem.mp4", "stml", "stmp", "stmx", "stn=", "stpl", "stplz", "strg", "strings", "stuff", "stxt", "style", "sucatalog", "suml", "sumo", "supported", "svcd", "svdl", "svslide", "swdb", "swdoc", "swf2", "swfl", "swgr", "swift", "switch", "swss", "sxls", "sxlsx", "sxml", "sylk", "syncdb-journal", "synciddb-journal", "synu", "sysml", "system", "szdd", "szproj", "t2flow", "t3001", "tabula-doc", "tar-gz", "tar-z", "tar.gz", "tar.xz", "tar.z", "taraa", "tardist", "taxform", "tbkx", "tbz2", "tceltx", "tda3mt", "tddd", "tdmb", "tdoc", "tdt2", "tdump", "teacher", "term", "texi", "text", "textclipping", "textile", "texture", "texturepack", "tfrd", "tfwx", "theater", "theme", "themepack", "thmb", "thmx", "thumb", "thumbindex", "thumbsdb", "tifenx", "tiff", "tifw", "tiger", "tile", "tivo", "tmdb", "tmprtf", "tmvt", "tmy2", "tnef", "tnsp", "tocg", "topc", "torrent", "totalsdb", "totalslayout", "totalssyncdb", "tpic", "tpoly", "tpsml", "tracwiki", "trash", "trec", "tria", "trib", "tridefmovie", "trif", "trx_dll", "tscproj", "tstream", "ttax", "ttbl", "ttkgp", "ttml", "ttpkg", "ttpl", "ttxt", "tvml", "tvod", "tvpi", "tvvi", "twbx", "twdx", "twiki", "tx3g", "txss", "txtenx", "txtrpt", "tzip", "udiwww", "ueaf", "ueed", "uenc", "ufdr", "ufs.uzip", "ugoira", "uhtml", "ulaw", "ulys", "unauth", "unif", "uninstall", "unitypackage", "uoml", "updf", "upload", "upoi", "uris", "url_", "urls", "user", "utf8", "utxt", "uvcab", "uvnts", "uvseg", "uyvy", "uzed", "uzip", "v11pf", "v264", "vala", "valu", "vbox", "vbox-extpack", "vbox-prev", "vbproj", "vcal", "vcard", "vclip", "vcls", "vcpf", "vcprj", "vcproj", "vdata", "vdb3", "vdjsample", "vdoc", "vdproj", "vep4", "vers", "vghd", "vhdl", "vicar", "video", "viewlet", "viff", "viivo", "vinf", "vivo", "vlab", "vlogo", "vmap", "vmcz", "vmdf", "vmdk", "vmlf", "vmlt", "vmsg", "vol1.egg", "vol5.egg", "vol8.egg", "volarchive", "voprefs", "vox-6k", "vox-8k", "voxal", "vp10", "vpdb", "vprj", "vproj", "vrge08contact", "vrge08event", "vrge08group", "vrge08message", "vrge08note", "vrml", "vrphoto", "vsdisco", "vsdm", "vsdx", "vsix", "vsmproj", "vsqx", "vssm", "vssx", "vstm", "vsto", "vstx", "vthought", "vxml", "w6bn", "w8bn", "w8tn", "waff", "walletx", "wand", "wapt", "waptt", "warc", "wavc", "wave", "wave64", "wbmp", "wbpz", "wbxml", "wcat", "wdbn", "wdcd", "wdgt", "wdoc", "wdseml", "weba", "webarchive", "webarchivexml", "webbookmark", "webdoc", "webhistory", "webintents", "webloc", "webm", "weboogl", "webp", "webpnp", "webpublishhistory", "website", "webtemplate", "webtest", "wfsp", "wgom", "whtt", "wifi", "wiki", "wireframe", "wizhtml", "wlmp", "wlpk", "wmdb", "wmlc", "wmlsc", "wmmp", "wmv3", "word", "workflow", "wp42", "wp50", "wpc2", "wpd0", "wpd1", "wpd2", "wpd3", "wpost", "wpostx", "wproj", "wrlk", "wsrc", "wsve", "wtbn", "wusiksnd", "wwcx", "wxmx", "x-png", "xaiml", "xavc", "xbap", "xbrl", "xcel", "xcon", "xdelta", "xdoc", "xdsl", "xfdf", "xfdl", "xgmml", "xhtm", "xhtml", "ximg", "xisb", "xisf", "xish", "xlam", "xlamenx", "xlbl", "xlc3", "xlc4", "xlc_", "xline", "xlist", "xlmv", "xlmx", "xlog", "xls3", "xls4", "xls5", "xls8", "xls_", "xlsb", "xlse", "xlsenx", "xlshtml", "xlsl", "xlsm", "xlsmhtml", "xlst", "xlsx", "xlsxe", "xlsxenx", "xlsxl", "xlthtml", "xltm", "xltx", "xlw3", "xlw4", "xlw5", "xlw_", "xlxml", "xmap", "xmcdz", "xmct", "xmdx", "xmind", "xmls", "xmltv", "xmlx", "xmmas", "xmmat", "xmmmp", "xmod", "xmpz", "xosm", "xpak", "xpng", "xpr3", "xprj", "xpwe", "xrds", "xrm-ms", "xrns", "xslb", "xslt", "xsml", "xspf", "xtea", "xtml", "xtodvd", "xtps", "xvag", "xvid", "xweb3asax", "xweb3htm", "xweb4shtml", "xwma", "xwmv", "xy4v", "xyzi", "xzfx", "xzip", "y8pd", "yaml", "yaws", "yaz0", "ybhtm", "ycbcra", "yenc", "yify", "ylib", "yookoo", "yrcbkm", "ytif", "zabw", "zanebug", "zargo", "zave", "zfsendtotarget", "zhtml", "zip2", "zipenx", "zipfs", "zipx", "zlas", "zlib", "zodb", "zpaq", "zpweb", "zrtf", "zsplit", "zx01", "zx02")


create_database = '''
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

CREATE TABLE Files (
    id                INTEGER  PRIMARY KEY,
    volume_id         INTEGER,
    extension         TEXT,
    extension_len     INTEGER,
    mtime             DATETIME,
    ctime             DATETIME,
    atime             DATETIME,
    crtime            DATETIME,
    size              INTEGER,
    blocks            NUMERIC,
    num_blocks        INTEGER,
    num_gaps          INTEGER,
    sum_gaps_bytes    INTEGER,
    sum_gaps_blocks   INTEGER,
    fragmented        BOOLEAN,
    backward          BOOLEAN,
    num_backward      INTEGER,
    resident          BOOLEAN,
    fs_compressed     BOOLEAN,
    sparse            BOOLEAN,
    linearconsecutive BOOLEAN,
    hardlink_id       INTEGER,
    num_hardlink      INTEGER,
    fs_seq            INTEGER,
    fs_nlink          INTEGER,
    fs_inode          INTEGER,
    CONSTRAINT lnk_Volumes_Files FOREIGN KEY (
        volume_id
    )
    REFERENCES Volumes (id),
    CONSTRAINT unique_id UNIQUE (
        id
    )
);

CREATE TABLE StorageDevices (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    system_id  INTEGER,
    model      TEXT,
    hwid       TEXT,
    size       INTEGER,
    rotational BOOLEAN,
    hotplug    BOOLEAN,
    CONSTRAINT lnk_Systems_StorageDevices FOREIGN KEY (
        system_id
    )
    REFERENCES Systems (id),
    CONSTRAINT unique_id UNIQUE (
        id
    )
);

CREATE TABLE Systems (
    id        INTEGER  PRIMARY KEY AUTOINCREMENT,
    start_run DATETIME,
    end_run   DATETIME,
    os        TEXT,
    CONSTRAINT unique_id UNIQUE (
        id
    )
);

CREATE TABLE Volumes (
    id                INTEGER PRIMARY KEY,
    storage_device_id INTEGER,
    fs_type           TEXT,
    size              INTEGER,
    used              INTEGER,
    free              INTEGER,
    block_size        INTEGER,
    flags             TEXT,
    CONSTRAINT lnk_StorageDevices_Volumes FOREIGN KEY (
        storage_device_id
    )
    REFERENCES StorageDevices (id),
    CONSTRAINT unique_id UNIQUE (
        id
    )
);

CREATE INDEX index_deviceid ON Volumes (
    "storage_device_id"
);

CREATE INDEX index_instanceid ON StorageDevices (
    "system_id"
);

CREATE INDEX index_volumeid ON Files (
    "volume_id"
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;'''
