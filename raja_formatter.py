
class Formatter():
    def __init__(self,placeholder_string,*args, **kwargs):
        self.placeholder_string = placeholder_string
        self.args = list(args)
        self.kwargs = kwargs

    def format_str(self):
        output_str = self.placeholder_string
        comma_separated_list = self.args
        key_based_args = self.kwargs

        if (len(self.args) == 0 and len(self.kwargs) == 0):
            return self.placeholder_string

        #replace all  the placeholders from the list
        for i, item in enumerate(comma_separated_list):
            search_str = "{" + str(i) + "}"
            if(search_str in output_str):
                position = output_str.index(str(i))
                output_str = output_str[:position-1] +" "+ item + " "+ output_str[position + 3:]

        for k,v in key_based_args.items():
            search_str = "{" + str(k) + "}"
            if (search_str in output_str):
                position = output_str.index(str(k))
                output_str = output_str[:position - 1] + " " + v + " " + output_str[position + len(k) + 1:]

        return output_str

if __name__ == "__main__":

    formatter = Formatter("name is {0} and  sur is {surname}", "raja" ,surname = 'bade')
    print (formatter.format_str())
    print("success")
