import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:peladas/configuracao_details.dart';
import 'package:peladas/data/data.dart';
import 'package:peladas/main.dart';
import 'package:peladas/peladaDetalhe.dart';
import 'package:shared_preferences/shared_preferences.dart';

class Str {
  String text;
  Str({this.text});
}

class detalhes extends StatelessWidget {
  Api api = Api();
  SharedPreferences prefs;

  final int id;
  final String token;
  detalhes({Key key, this.id, this.token}) : super(key: key);

  final List<Str> data = <Str>[
    Str(text: "Configurações"),
    Str(text: "Jogadores"),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.white,
        title: Center(
          child: Text("Pelada",
              style: new TextStyle(
                  color: Colors.red, fontWeight: FontWeight.normal)),
        ),
        automaticallyImplyLeading: false,
      ),
      body: new Container(
        child: new FutureBuilder<Configuracao>(
            future: api.getConfiguracao(this.token, this.id),
            builder: (context, snapshot) => new FutureBuilder<PeladaDetalhe>(
                  future: api.peladaDetalhe(this.token, this.id),
                  builder: (context, detalhes) => new Column(
                          mainAxisAlignment: MainAxisAlignment.start,
                          children: <Widget>[
                            InkWell(
                              onTap: () {
                                Navigator.push(
                                  context,
                                  CupertinoPageRoute(
                                      builder: (context) => JogadoresScreen(
                                            pelada: detalhes.data,
                                          )),
                                );
                              },
                              child: Card(
                                child: ListTile(
                                  leading: const Icon(Icons.playlist_play),
                                  title: Text("Jogadores"),
                                ),
                              ),
                            ),
                            InkWell(
                              onTap: () {
                                Navigator.push(
                                  context,
                                  CupertinoPageRoute(
                                      builder: (context) =>
                                          ConfiguracaoDetailScreen(
                                            configuracao: snapshot.data,
                                          )),
                                );
                              },
                              child: Card(
                                  child: ListTile(
                                      leading: const Icon(Icons.settings),
                                      title: Text("Configurações"))),
                            )
                          ]),
                )),
      ),
    );
  }
}
