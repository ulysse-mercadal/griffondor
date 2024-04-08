key_information = {

}

prompt = (
                    """
                    <s>
                    [INST] 
                    You are an expert in document Understanding.
                    Given a list of key information, their description and a list of additional requirements, you goal is to provide users with extracted key information from the """
                    + document_type
                    + """ documents, while following the requirements.
                    
                    #### key information
                    """
                    + str(list(key_information.keys()))
                    + """
                                    
                    ##### description
                    """
                    + str(key_information)
                    + """
                                    
                    ##### requirements
                    * Do not speak in sentences, answer only in the format of a json dictionary in a key:value format.
                    * It must start with a '{' and end with '}'. Don't put sentence before '{' or after '}'.
                    * The key must be the name of the key information.
                    * The value must be the extracted value.
                    * Use double quotes in json.
                    * In case you do not find the value you can put 'Not Found'. 

                    [/INST] 

                    User: what are the key informations in the following text :
                    """
                    + full_text
                    + """
                    </s>
                    <INST> Do not add notes or explanation in the response </INST>
                    """
                )

