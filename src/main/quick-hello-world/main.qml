import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.15

Window {
    id: window
    visible: true
    width: 640
    height: 480
    color: "#ffffff"
    property alias label: label
    property alias button: button
    title: qsTr("Hello World")

    Button {
        id: button
        text: qsTr("Apply")
        anchors.verticalCenterOffset: 0
        anchors.horizontalCenterOffset: 42
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter

        Connections {
            target: button
            onClicked: label.text = textInput.text
        }
    }

    Label {
        id: label
        y: 157
        width: 38
        height: 18
        text: "______"
        anchors.horizontalCenter: parent.horizontalCenter
    }

    TextInput {
        id: textInput
        x: 209
        width: 80
        height: 20
        text: qsTr("")
        anchors.verticalCenterOffset: 0
        verticalAlignment: Text.AlignVCenter
        anchors.verticalCenter: parent.verticalCenter
        anchors.right: button.left
        anchors.rightMargin: 31
        font.pixelSize: 12

        Connections {
            target: textInput
            onEditingFinished: label.text = textInput.text
        }
    }
}
