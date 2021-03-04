#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include "hangman.h"
#include "QMessageBox"
#include "QInputDialog"
#include "QGraphicsEllipseItem"

MainWindow::MainWindow(QWidget *parent): QMainWindow(parent), ui(new Ui::MainWindow) {
    ui->setupUi(this);

    // ask wether to use multiplayer
    QMessageBox msgBox;
    msgBox.setWindowTitle(tr("Hangman - Multiplayer?"));
    msgBox.setText(tr("Would you like to let the application chose a word for you?"));
    msgBox.setStandardButtons(QMessageBox::Yes | QMessageBox::No);
    msgBox.setDefaultButton(QMessageBox::No);
    int ret = msgBox.exec();

    // if multiplayer, let the user define the solution
    hangman = new Hangman;
    if(ret == QMessageBox::No) {
        bool ok;
        QString solution = QInputDialog::getText(this, tr("QInputDialog::getText()"),
                                                                  tr("Solution:"), QLineEdit::Normal,
                                                                  "", &ok);
        ok = checkInput(solution);
        if(ok) hangman->setSolution(solution);
    }

    // setup the image

    // create pen and use color of text
    QPen pen = QPen(QWidget::palette().color(QPalette::WindowText));

    QGraphicsEllipseItem *ground = scene.addEllipse(-50, 0, 100, 50, pen);
    ground->setStartAngle(0);
    ground->setSpanAngle(180*16);
    ground->setVisible(false);

    QGraphicsLineItem *pole = scene.addLine(0, 0, 0, -50, pen);
    pole->setVisible(false);

    QGraphicsLineItem *hanger = scene.addLine(0, -50, 50, -50, pen);
    hanger->setVisible(false);

    QGraphicsLineItem *rope = scene.addLine(50, -50, 50, -25, pen);
    rope->setVisible(false);

    // construct a hangman using a item group
    QGraphicsItemGroup* hanging_man = new QGraphicsItemGroup;
    // body
    QGraphicsLineItem* body = new QGraphicsLineItem(0, 0, 0, 20);
    body->setPen(pen);
    hanging_man->addToGroup(body);
    // head
    QGraphicsEllipseItem* head = new QGraphicsEllipseItem(-5, -10, 10, 10);
    head->setPen(pen);
    hanging_man->addToGroup(head);
    // left leg
    QGraphicsLineItem* leg_l = new QGraphicsLineItem(0, 20, -5, 40);
    leg_l->setPen(pen);
    hanging_man->addToGroup(leg_l);
    // right leg
    QGraphicsLineItem* leg_r = new QGraphicsLineItem(0, 20, 5, 40);
    leg_r->setPen(pen);
    hanging_man->addToGroup(leg_r);

    hanging_man->setVisible(false);
    hanging_man->setPos(50, -25);
    scene.addItem(hanging_man);

    // show the information
    ui->labelStatus->setText(hangman->getStatus());
    ui->pictureStatus->setScene(&scene);
    updateStatus();
}

MainWindow::~MainWindow() {
    delete ui;
    hangman->~Hangman();
}

void MainWindow::end(bool win) {
    // show a popup which asks wether to restart
    QMessageBox msgBox;
    msgBox.setWindowTitle("Hangman - The End");
    msgBox.setIcon(QMessageBox::Question);
    QString message;
    if(win) {
        message = tr("You won!");
    } else {
        message = tr("You lose. The solution was: ") + hangman->getSolution();
    }
    message.append("\n" + tr("Start a new game?"));
    msgBox.setText(message);
    msgBox.setStandardButtons(QMessageBox::Yes | QMessageBox::No);
    msgBox.setDefaultButton(QMessageBox::Yes);
    int ret = msgBox.exec();

    // decide what to do next based on button selection
    switch (ret) {
        case QMessageBox::Yes:
            // restart
            hangman = new Hangman("");
            // show the information
            ui->labelStatus->setText(hangman->getStatus());
            updateStatus();
            break;
        case QMessageBox::No:
            // quit the game
            QApplication::quit();
        default:
            break;
    }
}

void MainWindow::updateStatus() {
    // update statusbar
    statusBar()->showMessage(QString("You have %1 tries left. Letters tried: %2").arg(hangman->getTriesLeft()).arg(hangman->getGuessed()));

    // update image
    QList<QGraphicsItem *> items = ui->pictureStatus->scene()->items();

    if(hangman->getTriesLeft()>4){
        for(QGraphicsItem *item : scene.items()) {
            item->setVisible(false);
        }
    } else {
        if(hangman->getTriesLeft()<=4) items.at(8)->setVisible(true);
        if(hangman->getTriesLeft()<=3) items.at(7)->setVisible(true);
        if(hangman->getTriesLeft()<=2) items.at(6)->setVisible(true);
        if(hangman->getTriesLeft()<=1) items.at(5)->setVisible(true);
        if(hangman->getTriesLeft()<=0) items.at(4)->setVisible(true);
    }
}

// slots

void MainWindow::check() {
    // get input and check content
    QString input = ui->inputGuess->text();
    if(!checkInput(input)) return;

    // only look at first character
    QChar c = input.at(0);

    switch (hangman->check(c)) {
        case -2:
            // no guesses left
            updateStatus();
            end(false);
            break;
        case -1:
            // guess is false
            updateStatus();
            break;
        case 0:
            // already guessed
            break;
        case 1:
            // guess is correct
            ui->labelStatus->setText(hangman->getStatus());
            updateStatus();
            break;
        case 2:
            // guessed the entire word
            ui->labelStatus->setText(hangman->getStatus());
            updateStatus();
            end(true);
            break;
        default:
            break;
    }

    // empty input widget
    ui->inputGuess->clear();
}

void MainWindow::skip() {
    end(false);
}

bool MainWindow::checkInput(QString input) {
    if(input.length() <= 0 || !input.isSimpleText()){
        // show a popup with a warning
        QMessageBox msgBox;
        msgBox.setWindowTitle("Hangman - Invalid input");
        msgBox.setIcon(QMessageBox::Warning);
        msgBox.setText("Simple text is the only valid input");
        msgBox.exec();
        return false;
    }
    else return true;
}
