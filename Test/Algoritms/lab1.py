from random import randint
import datetime


class Man:
    is_paired = False
    woman_number = 0

    def __init__(self, education, name):
        self.education = education
        self.name = name

    def show_education(self):
        print(self.education)

    def get_name(self):
        return self.name


class Woman(Man):
    is_paired = False
    man_education = 0
    man_number = 0

    def __init__(self, education, name):
        super().__init__(education, name)
        self.man_education = 0

    def get_man_education(self):
        return self.man_education


def creating_men(pairs_number):
    men_list = []
    print("creating a list of men")
    for obj in range(pairs_number):
        man = Man(randint(60, 100), "man" + str(obj))
        men_list.append(man)
        print(man.get_name())
    print(men_list)
    print("education of men")
    for x in range(len(men_list)):
        men_list[x].show_education()

    return men_list


def creating_women(pairs_number):
    women_list = []
    print("\ncreating a list of women")
    for obj in range(pairs_number):
        women = Woman(randint(60, 100), "woman" + str(obj))
        women_list.append(women)
        print(women.get_name())

    print(women_list)
    print("education of women")
    for x in range(len(women_list)):
        women_list[x].show_education()

    return women_list
def debag(men_list,women_list):
    for i in range(len(men_list)):
        print(men_list[i].name, "in pair:", men_list[i].is_paired, "education", men_list[i].education,
              "with", women_list[men_list[i].woman_number].name, "education",
              women_list[men_list[i].woman_number].education)

def creating_pairs(men_list, women_list):
    print("Pairing people...\n", men_list, "\n", women_list)
    for x in range(9):
       # debag(men_list,women_list)
        for i in range(len(men_list)):
            current_women_education = 0
            current_women_number = 0
            for j in range(len(women_list)):
                if women_list[j].education > current_women_education and women_list[j].man_education < men_list[i].education:
                    current_women_education = women_list[j].education
                    current_women_number = j
                    men_list[women_list[current_women_number].man_number].is_paired = T
                    #debag(men_list, women_list)

            # запись education и номера мужчины в женщину и обнунуление соперника
            women_list[current_women_number].man_education = men_list[i].education
            men_list[i].woman_number = current_women_number
            men_list[i].is_paired = True
            women_list[current_women_number].man_number = i
            debag(men_list, women_list)

    for i in range(len(men_list)):
        print(men_list[i].name, "in pair:", men_list[i].is_paired, "education", men_list[i].education,
              "with", women_list[men_list[i].woman_number].name, "education",
              women_list[men_list[i].woman_number].education)



pairs_number = int(input("Enter number of pairs:"))
start = datetime.datetime.today()
creating_pairs(creating_men(pairs_number), creating_women(pairs_number))
end = datetime.datetime.today()
print(end - start)