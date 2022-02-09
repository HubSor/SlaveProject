PATH = "./SlaveProjectUE/Content/Data/"

def format_string(names):
    result = "\"("
    for name in names:
        result += f"\"\"{name}\"\","
    result = result[:-1]
    result += ")\""
    return result

def export_names_to_csv(recordName, namesM, namesF, race = "Human", filename = "names.csv", path = PATH):
    f = open(path + filename, "w")
    f.write(",NamesM,NamesF,Race\n")
    formatted_m = format_string(namesM)
    formatted_f = format_string(namesF)
    formatted_r = f"\"{race}\""
    f.write(f"{recordName},{formatted_m},{formatted_f},{formatted_r}")
    f.close()

def export_surnames_to_csv(recordName, surnames, race = "Human", filename = "surnames.csv", path = PATH):
    f = open(path + filename, "w")
    f.write(",Surnames,Race\n")
    formatted_m = format_string(surnames)
    formatted_r = f"\"{race}\""
    f.write(f"{recordName},{formatted_m},{formatted_r}")
    f.close()

def export_nicknames_to_csv(recordName, nicks, race = "Human", filename = "nicknames.csv", path = PATH):
    f = open(path + filename, "w")
    f.write(",Nicknames,Race\n")
    formatted_m = format_string(nicks)
    formatted_r = f"\"{race}\""
    f.write(f"{recordName},{formatted_m},{formatted_r}")
    f.close()

class NameGenerator:
    def __init__(self) -> None:
        pass

    def generate_nicknames(self):
        adjectives = ["Strong","Great","Tall","Big","Black","Red","White","Blue","Golden","Gold","Silver","Wise",
            "Old","Young","Greedy","Bloody","Furious","Tall","Short","Small","Dark","Shadow","Honorable","Venomous",
            "Poisonous","Green","Mythical","Legendary","Epic","Romantic","Just","Stern","Pious","Holy","Dreadful",
            "Fearful","Horrid","Awful","Cruel","Ferocious","Savage","Grim","Sad","Fierce","Saint","Blind","Laughing",
            "Crazy","Posessed","Deluded","Crazed","Mad","Titanous","Monstrous","Gory","Immortal","Ancient","Fiery",
            "Solid","Noble","Gentle","Proud","Ruthless","Sharp","Dull"]
        objects = ["Lion","Bear","Eagle","Dragon","Hydra","Tower","Wolf","Hyena","Frog","Bull","Stag","Heart","Face",
            "Fox","Rose","King","Prince","Ruler","Fighter","Monk","Priest","Cannibal","Assasin","Giant","Death","Empereor",
            "Leopard","Tiger","Tryton","Watcher","Guardian","Ranger","Knight","Sun","Storm","Demon","Devil","Monster",
            "Creature","Creation","Mutant","Predator","Viper","Snake","Bastard","Maniac","Abomination","Hunter","Bowman",
            "Armorer","Jouster","Gladiator","Kraken","Behemoth","Leviathan","God","Brother","Husband","Son","Faher",
            "Messiah","Redeemer","Entertainer","Jester","Berserker","Refuge","Pilgrim","General","Spider","Bird",
            "Flame","Traitor","Machine","Rock","Boulder","Falcon","Parrott","Pirate","Count","Lord","Seahorse","Horse",
            "Stalion","Fish","Shark","Crane","Offender","Aggressor","Conqueror","Invader","Dominator","Raven","Tree",
            "Wall","Shield","Sword","Axe","Fist","Spear","Knife","Dagger","Bow","Crossbow","Lance","Hornet","Stone",
            "Mountain","Hound","Dog","Cat","Panther","Harpy","Explorer","Master"]

        results = []
        [results.append(word) for word in adjectives]
        [results.append(word) for word in objects]
        for adj in adjectives:
            for obj in objects:
                results.append(adj + ' ' + obj)

        return results

    def generate_surnames(self):
        prefixes = ["Long","Short","Black","White","Red","Dark","Shield","Sword","Bone","Sun","Ice","Rain","Flame",
            "Plain","Green","Frost","Ash","Man","Will","Fork","Storm","Grey","Dusk","Rose","Butter","Wood","Mac",
            "Arm","Great","Lann","Gold","Dread","Turn","Good","Under","Brandy","Proud","Finn","Loth","Clay","Hedge",
            "Far","Cotton","Silver","Bronze","Holy","Town","Mayor","Puddle","Mar","Lang","Two","Ham","Har","Hay",
            "Wagel","Wegel","Heis","Over","Frieg","Shore"]
        postfixes = ["wood","beard","hollow","blood","brook","ish","joy","iron","steel","vale","en","son","sen",
            "strong","ster","theon","ery","berry","barry","buck","sell","bottom","foot","ins","hill","belly",
            "bridge","man","men","mans","mons","idge","wort", "burrow","hanger","gund","hopper","rans","ran","run",
            "field","send","smith","phin","ton","ten","walker","ward","heim","rich","berg","hagen","tons","fer","ber",
            "ller","lar","land","e","bud","well"]

        results = []
        for pref in prefixes:
            for post in postfixes:
                results.append(pref + post)

        return results

    def generate_names(self, b_masculine = True):
        first_letters = "WRTPSDGHJLZVBM"
        second_letters = "aeoui"
        connectors = "rtpsdglbnm"
        suffixes_1 = "aioeu"
        suffixes_2 = "rsdlbmn"

        results = []

        for l1 in first_letters:
            for l2 in second_letters:
                for l3 in connectors:
                    for l4 in suffixes_1:
                        for l5 in suffixes_2:
                            if b_masculine:
                                results.append(l1 + l2 + l3 + l4 + l5)
                            else:
                                results.append(l1 + l2 + l3 + l4 + l5 + 'a')
                    for l4 in suffixes_1:
                        for l5 in suffixes_2:
                            if b_masculine:
                                results.append(l1 + l2 + l3 + 'r' + l4 + l5)
                            else:
                                results.append(l1 + l2 + l3 + 'r' + l4 + l5 + 'a')
        return results

if __name__ == "__main__":
    gen = NameGenerator()
    # surnames = gen.generate_surnames()
    # print(surnames, len(surnames))
    # export_surnames_to_csv("HumanSurnames", surnames)

    # m_names = gen.generate_names()
    # f_names = gen.generate_names(False)
    # export_names_to_csv("HumanNames", m_names, f_names)

    nicks = gen.generate_nicknames()
    print(nicks, len(nicks))
    # export_nicknames_to_csv("HumanNicknames",nicks)
