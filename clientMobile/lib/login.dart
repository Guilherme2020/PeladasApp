import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:peladas/data/data.dart';
import 'package:peladas/data/principal.dart';
import 'package:peladas/main.dart';

class loginScreen extends StatefulWidget {
  @override
  _MyCustomFormState createState() => _MyCustomFormState();
}

class _MyCustomFormState extends State<loginScreen> {
  final email = TextEditingController();
  final senha = TextEditingController();
  Api api = Api();

  @override
  void dispose() {
    // Clean up the controller when the Widget is disposed
    email.dispose();
    senha.dispose();
    super.dispose();
  }

  void _callSubmit(String token) {
    var api = new Api();
    api.postJogador('nome', 1, '1', token);
  }

  @override
  Widget build(BuildContext context) {
    final key = new GlobalKey<ScaffoldState>();

    return Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.white,
          title: Center(
            child: Text("Entrar com o email",
                style: new TextStyle(
                    color: Colors.red, fontWeight: FontWeight.normal)),
          ),
          automaticallyImplyLeading: false,
        ),
        body: Column(
          children: <Widget>[
            Padding(
              padding: EdgeInsets.all(16.0),
              child: TextFormField(
                decoration: InputDecoration(
                    labelText: 'Email',
                    fillColor: Colors.red,
                    labelStyle: TextStyle(color: Colors.red),
                    hintStyle: new TextStyle(color: Colors.red)),
                controller: email,
              ),
            ),
            Padding(
              padding: EdgeInsets.all(16.0),
              child: TextFormField(
                decoration: InputDecoration(
                    labelText: 'Senha',
                    labelStyle: TextStyle(color: Colors.red),
                    hintStyle: TextStyle(color: Colors.red)),
                controller: senha,
              ),
            ),
            new Container(
              child: new FutureBuilder<User>(
                future: api.usuario(email.text, senha.text),
                builder: (context, snap) => Padding(
                      padding: const EdgeInsets.all(16.0),
                      child: InkWell(
                        onTap: () {
                          if (snap.hasData != false) {
                            Navigator.push(
                              context,
                              new MaterialPageRoute(
                                builder: (context) => PrincipalScreen(
                                      user: snap.data,
                                    ),
                              ),
                            );
                          } else {
                            final snackBar = SnackBar(
                                content: Text(
                                    'Informe o login e senha correto' +
                                        snap.toString()));
                            Scaffold.of(context).showSnackBar(snackBar);
                          }
                        },
                        child: ButtonTheme(
                          minWidth: double.infinity,
                          child: MaterialButton(
                            color: Colors.red,
                            child: Text('Entrar',
                                style: new TextStyle(
                                    color: Colors.white, fontFamily: 'Heavy')),
                          ),
                        ),
                      ),
                    ),
              ),
            )
          ],
        ));
  }
}
