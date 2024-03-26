from flask import Flask, render_template, request, redirect, url_for, flash
from article import Article
from comment import Comment

app = Flask(__name__)
app.secret_key = 'secret_key'

Article("Cele mai recente tehnologii în domeniul AI", "În informatică, inteligența artificială (IA) este inteligența "
                                                      "mașinilor, spre deosebire de inteligența naturală de la oameni "
                                                      "și animale. Informatica definește cercetarea IA ca studiu al "
                                                      "„agenților inteligenți⁠(d)”: orice dispozitiv care își percepe "
                                                      "mediul și efectuează acțiuni care maximizează șansa de a-și "
                                                      "atinge cu succes obiectivele. Mai exact, "
                                                      "Kaplan și Haenlein definesc IA ca fiind „capacitatea unui "
                                                      "sistem de a interpreta corect datele externe, de a învăța din "
                                                      "astfel de date și de a folosi ceea ce a învățat pentru a-și "
                                                      "atinge obiective și sarcini specifice printr-o adaptare "
                                                      "flexibilă”.[3] Termenul „inteligență artificială” este "
                                                      "utilizat colocvial pentru a descrie mașinile care imită "
                                                      "funcțiile cognitive pe care le asociază oamenii cu alte minți "
                                                      "umane, cum ar fi „învățarea” și „rezolvarea problemelor”.[4]["
                                                      "5] Inteligența artificială implică dezvoltarea de algoritmi și "
                                                      "modele care permit mașinilor să-și perceapă mediul, "
                                                      "să își motiveze mediul și să facă acțiuni adecvate pentru a "
                                                      "atinge obiective specifice. Acești algoritmi folosesc volume "
                                                      "mari de date și tehnici avansate, cum ar fi învățarea "
                                                      "automată, învățarea profundă, procesarea limbajului natural și "
                                                      "viziunea computerizată.Află mai multe despre ultimele tendințe "
                                                      "și tehnologii din domeniul inteligenței "
                                                      "artificiale.Inteligența artificială fără cod, cu interfețele "
                                                      "sale ușoare de tip drag-and-drop, va permite oricărei companii "
                                                      "să-și folosească puterea pentru a crea produse și servicii mai "
                                                      "inteligente. Vedem deja această tendință pe piața de retail. "
                                                      "Stitch Fix folosește algoritmi activați cu inteligență "
                                                      "artificială pentru a recomanda clienților săi haine care se "
                                                      "potrivesc cu mărimile și gusturile acestora. Cumpărăturile și "
                                                      "livrarea autonome, fără contact, vor fi, de asemenea, "
                                                      "o tendință uriașă pentru 2023. IA va face mai ușoare pentru "
                                                      "consumatori plata și primirea de bunuri și servicii. IA va "
                                                      "spori, de asemenea, aproape fiecare loc de muncă din fiecare "
                                                      "proces de afaceri din industrii. Mai mulți comercianți cu "
                                                      "amănuntul vor folosi inteligența artificială pentru a gestiona "
                                                      "și automatiza procesele complexe de gestionare a stocurilor "
                                                      "care au loc în culise, astfel încât tendințele de comoditate "
                                                      "cum ar fi buy-online-pickup-at-curbside (BOPAC), "
                                                      "buy-online-pickup-in-store (BOPIS), "
                                                      "iar buy-online-return-in-store (BORIS) va deveni un lucru "
                                                      "standard. Inteligența artificială va fi, de asemenea, "
                                                      "motorul din spatele celor mai noi inițiative de livrare "
                                                      "autonomă pe care comercianții cu amănuntul le pilotează și le "
                                                      "lansează, iar din ce în ce mai mulți lucrători din retail vor "
                                                      "trebui să se obișnuiască să lucreze alături de mașinării.")
Article("Arta abstractă și expresionistă în secolul XXI", "Renașterea a debutat în secolele XIV-XVI, perioada Evului "
                                                          "Mediu Târziu, în Florența - Italia și s-a răspândit în "
                                                          "restul Europei. Această mișcare culturală reprezintă "
                                                          "înflorirea inovatoare a literaturii latine și autohtone, "
                                                          "începând din secolul al XIV-lea, când erau cercetate "
                                                          "sursele literare din antichitatea clasică creditată lui "
                                                          "Francesco Petrarca. Dezvoltarea în pictură a tehnicilor de "
                                                          "perspectivă, de acordare a unei realități mult mai "
                                                          "naturale a dus și la o reformă educațională. Schimbările "
                                                          "Renașterii nu au fost implementate uniform de întreaga "
                                                          "Europă, deși apariția tiparului a accelerat difuzarea "
                                                          "ideilor în secolul al XV-lea. Descoperă operele cele mai "
                                                          "remarcabile și inovative ale artiștilor din secolul XXI.")
Article("Cele mai controversate discutii despre AI", "Subiectele controversate de dezbatere sunt subiecte care pot "
                                                     "stârni opinii puternice și dezacorduri între oameni cu "
                                                     "convingeri și valori diferite. Aceste subiecte pot acoperi "
                                                     "diverse subiecte, cum ar fi probleme sociale, politică, "
                                                     "etică și cultură și pot contesta credințele tradiționale sau "
                                                     "normele stabilite""Un lucru care face ca aceste subiecte să fie "
                                                     "controversate este că adesea nu există un consens clar sau un "
                                                     "acord între oameni, ceea ce poate duce la dezbateri și dezacorduri."
                                                     "Fiecare persoană poate avea propria interpretare a faptelor sau "
                                                     "valorilor care îi influențează perspectiva. Este dificil pentru "
                                                     "toți să ajungă la o rezoluție sau un acord")
Article("Inteligența artificială amplifică amenințările de securitate", "Viitorul nu se anunţă deloc simplu pentru "
                                                                        "experţii din cybersecurity, iar creşterea "
                                                                        "numărului de specialişti IT şi nivelul lor "
                                                                        "de expertiză şi pregătire pentru a face faţă "
                                                                        "atacurilor trebuie să fie una dintre "
                                                                        "principalele măsuri adoptate de corporaţii "
                                                                        "şi guverne din întreaga lume. Din fericire, "
                                                                        "există în prezent multe resurse şi "
                                                                        "iniţiative care contribuie la formarea şi "
                                                                        "evoluţia specialiştilor din acest domeniu. "
                                                                        "Una dintre acestea este şi DefCamp unde, "
                                                                        "din 2011, sunt analizate în fiecare an cele "
                                                                        "mai noi tendinţe şi soluţii de "
                                                                        "cybersecurity. Astăzi, DefCamp este un hub "
                                                                        "al inovaţiei şi al colaborării în domeniul "
                                                                        "securităţii cibernetice, care adună la "
                                                                        "fiecare ediţie mii de participanţi din toată "
                                                                        "lumea, atât pasionaţi de securitate "
                                                                        "cibernetică, cât şi experţi, reprezentanţi "
                                                                        "ai instituţiilor, lideri ai companiilor şi "
                                                                        "ONG-urilor, şi studenţi. În plus, "
                                                                        "este şi o iniţiativă de a simplifica "
                                                                        "activitatea specialiştilor în securitate, "
                                                                        "dar, mai ales, de a împiedica şi limita "
                                                                        "eficienţa atacurilor cibernetice. ")
Article("Noua revoluţie care va hotărî cine va conduce lumea", "Majoritatea analiştilor tratează problema IA ca o "
                                                               "problemă a cursei tehnologice dintre SUA şi China. "
                                                               "Fără îndoială, mult din această competiţie se va "
                                                               "consuma în disputa directă americano-chineză, "
                                                               "date fiind atuurile de care am vorbit mai sus.  Se "
                                                               "neglijează, după opinia noastră, relevanţa prezenţei "
                                                               "ruseşti în această competiţie. Când Vladimir Putin "
                                                               "spune: „cine va deveni lider în domeniul inteligenţei "
                                                               "artificială, va conduce lumea” nu ne închipuim că a "
                                                               "făcut o asemenea afirmaţie de pe poziţia unui "
                                                               "comentator detaşat. Nu, a făcut-o ştiind că Rusia are "
                                                               "şi ea atuurile sale, mai mult că are anumite poziţii "
                                                               "deja câştigate. Nu este îndoială în această privinţă.")

# Exemple de comentarii pentru articole
Comment(1, "Articolul este foarte interesant! Sunt impresionat de progresul din domeniul AI.")
Comment(1, "Tehnologiile prezentate aici arată un viitor fascinant pentru inteligența artificială.")
Comment(2, "Arta abstractă este una dintre preferatele mele. Mulțumesc pentru acest articol informativ.")
Comment(2, "Ar fi minunat să vedem mai multe expoziții dedicate artei abstracte în viitorul apropiat.")
Comment(3, "Va recomand sa accesati (https://ahaslides.com/ro/blog/controversial-debate-topics/) pentru mai multe "
           "detalii")
Comment(3, "Ar fi minunat să vedem mai multe discutii despre acest subiect.")
Comment(4, "Dinamica de astăzi a tehnologiei susţine inovaţia, dar în acelaşi timp creşte şi riscurile de atacuri "
           "cibernetice asupra oamenilor, companiilor sau guvernelor.")
Comment(4, "În ultima vreme observăm şi creşterea tensiunilor geopolitice, astfel că nu trebuie să eliminăm nicio "
           "posibilitate. În faţa acestui tip de ameninţare")
Comment(5, "Articolul este foarte interesant! Sunt impresionat de progresul din domeniul AI.")
Comment(5, "Off ...Iar politica? ...offf.")


@app.route('/')
def index():
    articles = Article.get_all_articles()
    return render_template('index.html', articles=articles)


@app.route('/article/<int:article_id>', methods=['GET', 'POST'])
def view_article(article_id):
    article = Article.get_article_by_id(article_id)
    comments = Comment.get_comments_for_article(article_id)
    additional_info = "Aici puteți adăuga text suplimentar pentru articolul curent."

    if request.method == 'POST':
        content = request.form['content']
        if content not in [comment.content for comment in comments]:
            new_comment = Comment(article_id, content)
            new_comment.save()
        else:
            flash('Comentariul există deja!', 'error')

        return redirect(url_for('view_article', article_id=article_id))

    unique_comments = set(comment.content for comment in comments)
    return render_template('article.html', article=article, comments=unique_comments, additional_info=additional_info)


@app.route('/add_article', methods=['GET', 'POST'])
def add_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_article = Article(title, content)
        new_article.save()
        return redirect(url_for('index'))
    return render_template('add_article.html')


@app.route('/article/<int:article_id>/add_comment', methods=['POST'])
def add_comment(article_id):
    content = request.form['content']
    existing_comments = Comment.get_comments_for_article(article_id)

    # Verificăm dacă comentariul există deja în lista de comentarii pentru articolul respectiv
    if content not in [comment.content for comment in existing_comments]:
        new_comment = Comment(article_id, content)
        new_comment.save()
    else:
        # Dacă comentariul este duplicat, afișăm un mesaj de eroare utilizatorului
        flash('Comentariul există deja!', 'error')

    return redirect(url_for('view_article', article_id=article_id))


if __name__ == '__main__':
    app.run(debug=True)
