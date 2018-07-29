from django.shortcuts import render
from django.http import HttpResponse, request
from django.utils.decorators import method_decorator
from django.views import View

from contact.models import Person, Address, Phone, Group, Email
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def new_person_form():
    form = """
                <html><body><form action='#' method='POST'>
                Dodaj nowa osobę: <br><br>
                <label> Imię:<br>
                    <input type='text' name='name'>
                </label><br>
                <label> Nazwisko:<br>
                    <input type='text' name='surname'>
                </label><br>
                <label> Opis:<br>
                    <input type='text' name='description'>
                </label><br>
                <input type='submit' value='Wyślij'>
                </form></body></html>
                """
    return form


def modify_person(name, surname, description, id):
    form = """
            <html><body><form action='#' method='POST'>
                Zmień dane {} {} <br><br>
                <label> Imię:<br>
                    <input type='text' name='name' value='{}'>
                </label><br>
                <label> Nazwisko:<br>
                    <input type='text' name='surname' value='{}'>
                </label><br>
                <label> Opis:<br>
                    <input type='text' name='description' value='{}'>
                </label><br>
                <input type='submit' value='Zapisz zmiany'><br>
                <a href='address/'>Dodaj adres</a><br>
                <a href='email/'>Dodaj email</a><br>
                <a href='phone/'>Dodaj numer telefonu</a>
                </form></body></html>
            """.format(name, surname, name, surname, description, id, id, id)
    return form


def add_address():
    form = """
            <html><body><form action='#' method='POST'>
            Dodaj adres<br>
            <label> Adres:<br>
                <input type='text' name='city' placeholder="Miasto"><br>
                <input type='text' name='street' placeholder="Ulica"><br>
                <input type='text' name='blockNumber' placeholder="Numer bloku"><br>
                <input type='text' name='apartmentNumber' placeholder="Numer mieszkania"><br>
            </label>
            <input type='submit' value='Zapisz zmiany'>
            </form></body></html>
            """
    return form


def modify_address(city, street, blockNumber, apartmentNumber):
    form = """
                <html><body><form action='#' method='POST'>
                Zmień adres<br>
                <label> Adres:<br>
                    <input type='text' name='city' value={}><br>
                    <input type='text' name='street' value={}><br>
                    <input type='text' name='blockNumber' value={}><br>
                    <input type='text' name='apartmentNumber' value={}><br>
                </label>
                <input type='submit' value='Zapisz zmiany'>
                </form></body></html>
                """.format(city, street, blockNumber, apartmentNumber)
    return form


def add_email():
    form = """
            <html><body><form action='#' method='POST'>
            Dodaj adres<br>
            <label> Email:<br>
                <input type='text' name='email'>
            </label>
            <label>Typ:
                    <select name="etype">
                        <option value="0">Niezindentyfikowany</option>
                        <option value="1">Domowy</option>
                        <option value="2">Służbowy</option>
                        <option value="3">Prywatny</option>
                    </select><br>
            </label>
            <input type='submit' value='Zapisz zmiany'>
            </form></body></html>
            """
    return form


def modify_email(email):
    form = """
            <html><body><form action='#' method='POST'>
            Zmień adres email<br>
            <label> Email:<br>
                <input type='text' name='email' value={}>
            </label>
            <label>Typ:
                    <select name="etype">
                        <option value="0">Niezindentyfikowany</option>
                        <option value="1">Domowy</option>
                        <option value="2">Służbowy</option>
                        <option value="3">Prywatny</option>
                    </select><br>
            </label>
            <input type='submit' value='Zapisz zmiany'>
            </form></body></html>
            """.format(email)
    return form


def add_phone():
    form = """
            <html><body><form action='#' method='POST'>
            Dodaj numer telefonu:<br>
            <label> Telefon:<br>
                <input type='number' name='number'>
            </label>
            <label>Typ:
                    <select name="phtype">
                        <option value="0">Niezindentyfikowany</option>
                        <option value="1">Domowy</option>
                        <option value="2">Służbowy</option>
                        <option value="3">Prywatny</option>
                    </select><br>
            </label>
            <input type='submit' value='Zapisz zmiany'>
            </form></body></html>
            """
    return form


def modify_phone(number):
    form = """
                <html><body><form action='#' method='POST'>
                Zmień numer telefonu:<br>
                <label> Telefon:<br>
                    <input type='number' name='number' value={}>
                </label>
                <label>Typ:
                        <select name="phtype">
                            <option value="0">Niezindentyfikowany</option>
                            <option value="1">Domowy</option>
                            <option value="2">Służbowy</option>
                            <option value="3">Prywatny</option>
                        </select><br>
                </label>
                <input type='submit' value='Zapisz zmiany'>
                </form></body></html>
                """.format(number)
    return form


def create_group():
    form = """
            <html><body><form action='#' method='POST'>
            Podaj nazwę grupy:
            <label>
                <input type='text' name='name'>
            </label> <br>
            <input type='submit' value='Wyślij'>
            </form></body></html>
            """
    return form


def modify_group(group_name):
    form = """
                <html><body><form action='#' method='POST'>
                Zmień nazwę grupy:
                <label>
                    <input type='text' name='name' value={}>
                </label> <br>
                <input type='submit' value='Wyślij'>
                </form></body></html>
                """.format(group_name)
    return form


@method_decorator(csrf_exempt, name='dispatch')
class NewPerson(View):
    def get(self, request):
        response = HttpResponse()
        response.write(new_person_form())
        return response

    def post(self, request):
        response = HttpResponse()
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        description = request.POST.get('description')
        Person.objects.create(name=name, surname=surname, description=description)
        response.write("""Dodano nową osobę: {} {} <br> <a href='/new/'>Dodaj kolejną osobę</a> <br>
                       <a href='/all/'>Powrót do listy osób</a>""".format(name, surname))
        return response


@method_decorator(csrf_exempt, name='dispatch')
class ModifyPerson(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        response = HttpResponse()
        response.write(modify_person(person.name, person.surname, person.description, id))
        return response

    def post(self, request, id):
        response = HttpResponse()
        person = Person.objects.get(id=id)
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        descritpion = request.POST.get('description')
        person.name = name
        person.surname = surname
        person.description = descritpion
        person.save()
        response.write("Zmieniono dane {} {} <br> <a href='/all/'>Powrót do listy osób</a>".format(person.name, person.surname))
        return response




@method_decorator(csrf_exempt, name='dispatch')
class DeletePerson(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        person.delete()
        response = "Osoba {} {} usunięta <br> <a href='/all/'>Powrót do listy osób</a>".format(person.name, person.surname)
        return HttpResponse(response)


@method_decorator(csrf_exempt, name='dispatch')
class PersonDetails(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        address = Address.objects.filter(person=person)
        email = Email.objects.filter(person=person)
        phone = Phone.objects.filter(person=person)
        answer = """
                <html><body>
                Szczegóły kontaktu:<br>
                    Imię: {} <br>
                    Nazwisko: {} <br>
                    Opis: {} <br>
                    <a href='/modify/{}'>Edytuj dane osobiste</a><br>
                """.format(person.name, person.surname, person.description, id)
        if len(address) > 0:
            for i in address:
                answer += """Adres: Miasto {}, ulica {} {}/{} 
                            <a href='/modify/{}/modify_address'>Edytuj</a>
                            <a href='/modify/{}/delete_address'>Usuń</a>
                            <br>""".format(i.city, i.street, i.blockNumber, i.apartmentNumber, person.id, person.id)
        if len(email) > 0:
            for i in email:
                answer += """Email: {}, typ: {} 
                            <a href='/modify/{}/modify_email'>Edytuj</a>
                            <a href='/modify/{}/delete_email'>Usuń</a>
                        <br>""".format(i.email, i.get_type_display(), person.id, person.id)
        if len(phone) > 0:
            for i in phone:
                answer += """Telefon: {}, typ: {}
                            <a href='/modify/{}/modify_phone'>Edytuj</a>
                            <a href='/modify/{}/delete_phone'>Usuń</a>
                        """.format(i.number, i.get_type_display(), person.id, person.id)
        answer += "</body></html>"
        return HttpResponse(answer)


@method_decorator(csrf_exempt, name='dispatch')
class AllPeople(View):
    def get(self, request):
        answer = """
                  <html><body>
                 Lista osób:<br>
                  <ol>
                  """
        persons = Person.objects.order_by('surname')
        for person in persons:
            answer += """<li>
                        <a href='/show/{0}/'> {1} {2}</a>
                        <a href='/modify/{0}/'>Edytuj</a>
                        <a href='/delete/{0}/'>Usuń</a>
                        </li>
                        """.format(person.id, person.surname, person.name)
        answer += """</ol> <a href='/new'>Dodaj nową osobę</a> <br>"""
        answer += "<a href='/create_group'>Dodaj nową grupę</a> <br>"
        answer += "<a href='/group_list'>Wyświetl grupy</a> <br>"
        answer += """<a href='/modify_group/{0}/'>Edytuj grupę</a> <br>
                    <a href='/delete_group/{0}/'>Usuń grupę</a>"""
        answer += "</body></html>"
        return HttpResponse(answer)


@method_decorator(csrf_exempt, name='dispatch')
class AddAddress(View):
    def get(self, request, id):
        response = HttpResponse()
        response.write(add_address())
        return response

    def post(self, request, id):
        person = Person.objects.get(id=id)
        response = HttpResponse()
        city = request.POST.get('city')
        street = request.POST.get('street')
        blockNumber = request.POST.get('blockNumber')
        apartmentNumber = request.POST.get('apartmentNumber')
        Address.objects.create(city=city, street=street, blockNumber=blockNumber, apartmentNumber=apartmentNumber,
                               person_id=person.id)
        response.write("Dodano nowy adres dla {} {} <br> <a href='/show/{}/'>Powrót</a>".format(person.name,
                                                                                                     person.surname, id))
        return response



@method_decorator(csrf_exempt, name='dispatch')
class ModifyAddress(View):
    def get(self, request, id):
        response = HttpResponse()
        person = Person.objects.get(id=id)
        address = Address.objects.filter(person=person)
        for i in address:
            response.write(modify_address(i.city, i.street, i.blockNumber, i.apartmentNumber))
        return response

    def post(self, request, id):
        response = HttpResponse()
        person = Person.objects.get(id=id)
        address = Address.objects.filter(person=person)
        city = request.POST.get('city')
        street = request.POST.get('street')
        blockNumber = request.POST.get('blockNumber')
        apartmentNumber = request.POST.get('apartmentNumber')
        for i in address:
            i.city = city
            i.street = street
            i.blockNumber = blockNumber
            i.apartmentNumber = apartmentNumber
            i.save()
        response.write("Zmieniono adres: {} {} <a href='/show/{}/'>Powrót</a>".format(person.name, person.surname, id))
        return response


@method_decorator(csrf_exempt, name='dispatch')
class DeleteAddress(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        address = Address.objects.filter(person=person)
        for i in address:
            i.delete()
        response = "Adres osoby {} {} usunięty <a href='/show/{}/'>Powrót</a>".format(person.name, person.surname, id)
        return HttpResponse(response)


@method_decorator(csrf_exempt, name='dispatch')
class AddEmail(View):
    def get(self, request, id):
        response = HttpResponse()
        response.write(add_email())
        return response

    def post(self, request, id):
        person = Person.objects.get(id=id)
        response = HttpResponse()
        email = request.POST.get('email')
        etype = request.POST.get('etype')
        Email.objects.create(email=email, type=etype, person_id=person.id)
        response.write("Dodano nowy email dla {} {} <br> <a href='/show/{}/'>Powrót</a>".format(person.name,
                                                                                                person.surname, id))
        return response


@method_decorator(csrf_exempt, name='dispatch')
class ModifyEmail(View):
    def get(self, request, id):
        response = HttpResponse()
        person = Person.objects.get(id=id)
        email = Email.objects.filter(person=person)
        for i in email:
            response.write(modify_email(i.email))
        return response

    def post(self, request, id):
        response = HttpResponse()
        person = Person.objects.get(id=id)
        email = Email.objects.filter(person=person)
        mail = request.POST.get('email')
        etype = request.POST.get('etype')
        for i in email:
            i.email = mail
            i.etype = etype
            i.save()
        response.write("Zmieniono adres email: {} {} <a href='/show/{}/'>Powrót</a>".format(person.name,
                                                                                            person.surname, id))
        return response


@method_decorator(csrf_exempt, name='dispatch')
class DeleteEmail(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        email = Email.objects.filter(person=person)
        for i in email:
            i.delete()
        response = "Adres email osoby {} {} usunięty <a href='/show/{}/'>Powrót</a>".format(person.name,
                                                                                            person.surname, id)
        return HttpResponse(response)


@method_decorator(csrf_exempt, name='dispatch')
class AddPhone(View):
    def get(self, request, id):
        response = HttpResponse()
        response.write(add_phone())
        return response

    def post(self, request, id):
        person = Person.objects.get(id=id)
        response = HttpResponse()
        number = request.POST.get('number')
        type = request.POST.get('phtype')
        Phone.objects.create(number=number, type=type, person_id=person.id)
        response.write("Dodano nowy numer telefonu dla {} {} <br> <a href='/show/{}/'>Powrót</a>".format(person.name,
                                                                                                person.surname, id))
        return response


@method_decorator(csrf_exempt, name='dispatch')
class ModifyPhone(View):
    def get(self, request, id):
        response = HttpResponse()
        person = Person.objects.get(id=id)
        phone = Phone.objects.filter(person=person)
        for i in phone:
            response.write(modify_phone(i.number))
        return response

    def post(self, request, id):
        response = HttpResponse()
        person = Person.objects.get(id=id)
        phone = Phone.objects.filter(person=person)
        number = request.POST.get('number')
        type = request.POST.get('phtype')
        for i in phone:
            i.number = number
            i.type = type
            i.save()
        response.write("Zmieniono numer telefonu: {} {}<a href='/show/{}/'>Powrót</a>".format(person.name,
                                                                                              person.surname, id))
        return response


@method_decorator(csrf_exempt, name='dispatch')
class DeletePhone(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        phone = Phone.objects.filter(person=person)
        for i in phone:
            i.delete()
        response = "Numer telefonu {} {} usunięty <a href='/show/{}/'>Powrót</a>".format(person.name, person.surname,
                                                                                         id)
        return HttpResponse(response)


@method_decorator(csrf_exempt, name='dispatch')
class CreateGroup(View):
    def get(self, request):
        response = HttpResponse()
        response.write(create_group())
        return response

    def post(self, request):
        response = HttpResponse()
        name = request.POST.get('name')
        Group.objects.create(name=name)
        response.write("Założono nową grupę: {}<br> <a href='/all/'>Powrót do listy osób</a>".format(name))
        return response


@method_decorator(csrf_exempt, name='dispatch')
class ModifyGroupName(View):
    def get(self, request, id):
        group = Group.objects.get(id=id)
        response = HttpResponse()
        response.write(modify_group(group))
        return response

    def post(self, request, id):
        response = HttpResponse()
        group = Group.objects.get(id=id)
        name = request.POST.get('name')
        group.name = name
        group.save()
        response.write("Zmieniono nazwę grupy na: {} <a href='/all/'>Powrót do listy osób</a>".format(name))
        return response


@method_decorator(csrf_exempt, name='dispatch')
class DeleteGroup(View):
    def get(self, request, id):
        group = Group.objects.get(id=id)
        group.delete()
        response = "Grupa {} usunięta <a href='/all/'>Powrót do listy osób</a>".format(group.name)
        return HttpResponse(response)


@method_decorator(csrf_exempt, name='dispatch')
class GroupList(View):
    def get(self, request):
        answer = """<html><body>
                Lista grup:<br>
                <ol>
                """
        group_list = Group.objects.order_by('name')
        for group in group_list:
            answer += """<li>
                        <a href='/show_group/{0}/'>{1}</a>
                        <a href='/modify_group/{0}/'>Edytuj grupę</a>
                        <a href='/delete_group/{0}/'>Usuń grupę</a>
                        </li>
                        """.format(group.id, group.name)
        answer += "</ol> <br> <a href='/all/'>Powrót do listy osób</a></body> </html>"
        return HttpResponse(answer)


@method_decorator(csrf_exempt, name='dispatch')
class Group(View):
    pass