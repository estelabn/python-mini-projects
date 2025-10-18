import json

if __name__ == '__main__':
    
    try:
        with open('input.json', 'r') as f:
            list_dict = json.loads(f.read())
        
        output = ','.join(list_dict[0])

        for element in list_dict:
            first = 0
            for id in element:
                if not first:
                    output += f'\n{element[id]}'
                else:
                    output += f',{element[id]}'
                first = 1
                
        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')