PATH = "./SlaveProjectUE/Content/Data/"

def format_names(names):
    result = "\"("
    for name in names:
        result += f"\"\"{name}\"\","
    result = result[:-1]
    result += ")\""
    return result

def export_to_csv(recordName, namesM, namesF, race = "Human", filename = "names.csv", path = PATH):
    f = open(path + filename, "w")
    f.write(",NamesM,NamesF,Race\n")
    formatted_m = format_names(namesM)
    formatted_f = format_names(namesF)
    formatted_r = f"\"{race}\""
    f.write(f"{recordName},{formatted_m},{formatted_f},{formatted_r}")
    f.close()

class NameGenerator:
    def __init__(self) -> None:
        self._first_letters = "WRTPSDGHJLZVBM"
        self._second_letters = "aeoui"
        self._connectors = "rtpsdglbnm"
        self._suffixes_1 = "aioeu"
        self._suffixes_2 = "rsdlbmn"

    def generate_name(self, b_masculine = True):
        results = []
        for l1 in self._first_letters:
            for l2 in self._second_letters:
                for l3 in self._connectors:
                    for l4 in self._suffixes_1:
                        for l5 in self._suffixes_2:
                            if b_masculine:
                                results.append(l1 + l2 + l3 + l4 + l5)
                            else:
                                results.append(l1 + l2 + l3 + l4 + l5 + 'a')
                    for l4 in self._suffixes_1:
                        for l5 in self._suffixes_2:
                            if b_masculine:
                                results.append(l1 + l2 + l3 + 'r' + l4 + l5)
                            else:
                                results.append(l1 + l2 + l3 + 'r' + l4 + l5 + 'a')
        return results

if __name__ == "__main__":
    gen = NameGenerator()
    m_names = gen.generate_name()
    f_names = gen.generate_name(False)
    export_to_csv("HumanNames", m_names, f_names)
