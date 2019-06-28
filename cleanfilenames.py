def clean_file_names(files):
    '''
    Filter out fields that are not necessary
    '''
    try:
        for file in files:

            current = str(file['filename']).split('/')[-1].lower()
            if '.' not in current:
                file['extlen'] = 0
                file['filename'] = ''
                continue

            if current.count('.') == 1:
                current = current.split('.')[-1]
                extlen = len(current)
                if extlen <= 3:
                    file['extlen'] = extlen
                    file['filename'] = current
                    continue

                name = ''
                for ext in static.extensions:
                    if current == ext:
                        name = ext
                        break
                file['filename'] = name
                file['extlen'] = extlen

            if current.count('.') == 2:
                current = current.split('.', 1)[-1]
                extlen = len(current)

                name = ''
                for ext in static.extensions:
                    if current == ext:
                        name = ext
                    file['filename'] = name
                    file['extlen'] = extlen
                
        return files
    except Exception as e:
        message("Runtime error during cleaning of file names.",
            log='error', display=False)
        logger.error(e, exc_info=True)
        message("\nRuntime error occurred, check log: " +
                config.logfile, log=None, display=True)
        exit()
