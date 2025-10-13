def checkListeArgs(listArgs):
    """
    Vérifie la validité de la liste d'arguments donnée.

    Retourne 1 si :
    - listArgs n'est pas une liste
    - listArgs est vide
    - Un des éléments de listArgs n'est ni un int ni un float

    Retourne None si la liste est valide.
    """
    if not isinstance(listArgs, list):
        return 1
    if len(listArgs) == 0:
        return 1
    for x in listArgs:
        if not isinstance(x, int) and not isinstance(x, float):
            return 1


class functions():
    """
    Classe regroupant plusieurs méthodes statistiques de base :
    - mean : moyenne
    - median : médiane
    - quartile : premier et troisième quartile
    - std : écart-type
    - var : variance
    """
    @classmethod
    def mean(cls, listArgs):
        """
        Calcule et affiche la moyenne des éléments de listArgs.

        Args:
            listArgs (list): Liste de valeurs numériques (int ou float).

        Returns:
            1 si la liste est invalide, sinon None.
        """
        if checkListeArgs(listArgs):
            return 1
        y = len(listArgs)
        i = sum(listArgs)
        print("mean :", i / y)
        return (i / y)

    @classmethod
    def median(cls, listArgs):
        """
        Calcule et affiche la médiane des éléments de listArgs.

        Args:
            listArgs (list): Liste de valeurs numériques.

        Returns:
            1 si la liste est invalide, sinon None.
        """
        if checkListeArgs(listArgs):
            return 1
        listArgs.sort()
        if len(listArgs) % 2:
            y = (len(listArgs) - 1) / 2
            print("median :", listArgs[int(y)])
        else:
            index = (len(listArgs) - 1) // 2
            y = (listArgs[index] + listArgs[index + 1]) / 2
            print("median :", y)

    @classmethod
    def quartile(cls, listArgs):
        """
        Calcule et affiche le premier et le troisième quartile d'une liste
        donnée.

        Args:
            listArgs (list): Liste de valeurs numériques.

        Returns:
            1 si la liste est invalide, sinon None.
        """
        if checkListeArgs(listArgs):
            return 1
        listArgs.sort()
        y = (1 / 4) * (len(listArgs) - 1)
        x = (3 / 4) * (len(listArgs) - 1)
        quartileList = [listArgs[int(y)], listArgs[int(x)]]
        print("quartile :", quartileList)

    @classmethod
    def std(cls, listArgs):
        """
        Calcule et affiche l'écart-type des éléments de listArgs.

        Args:
            listArgs (list): Liste de valeurs numériques.

        Returns:
            1 si la liste est invalide, sinon None.
        """
        if checkListeArgs(listArgs):
            return 1
        # the lenth of the value is the total population
        N = len(listArgs)
        # mean is nothing but adding all values and divide by total numbers
        mean = sum(listArgs)/N
        # finding (x-µ)² part- create a list with each value subtracted
        # by mean and squared
        NrSqr = [(x-mean)**2 for x in listArgs]
        # finding Σ portion which is nothing but all values sum
        Sigma = sum(NrSqr)
        # Square root to be taken for the sum
        Nr = Sigma ** (1/2)
        # taking square root to N for denominator
        Dr = N ** (1/2)
        # Find out standard deviation
        sd = Nr/Dr
        # Get output
        print("std :", sd)

    @classmethod
    def var(cls, listArgs):
        """
        Calcule et affiche la variance des éléments de listArgs.

        Args:
            listArgs (list): Liste de valeurs numériques.

        Returns:
            1 si la liste est invalide, sinon None.
        """
        if checkListeArgs(listArgs):
            return 1
        floatList = [float(x) if not isinstance(x, float)
                     else x for x in listArgs]
        mean = sum(floatList) / len(floatList)   # mean
        var = sum(pow(x-mean, 2) for x in floatList) / len(floatList)
        print("var :", var)
        return var


dict = {
    "mean": functions.mean,
    "median": functions.median,
    "quartile": functions.quartile,
    "std": functions.std,
    "var": functions.var
}


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Fonction principale qui applique les méthodes statistiques demandées sur
    les arguments fournis.

    Args:
        *args: Valeurs numériques à traiter.
        **kwargs: Arguments nommés indiquant quelles méthodes appliquer
        (par exemple: mean, median, var...).

    Raises:
        TypeError: Si une clé dans kwargs n'est pas une chaîne de caractères.

    Returns:
        None. Affiche les résultats directement.
    """
    for x in kwargs:
        if not isinstance(x, str):
            raise TypeError("kwargs must be str")
    listeArgs = list(args)
    for key, value in kwargs.items():
        if dict.get(value):
            if dict[value](listeArgs) == 1:
                print("ERROR")
        else:
            continue
