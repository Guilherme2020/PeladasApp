import 'dart:collection';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:peladas/data/data.dart';
import 'package:peladas/edit_configuracao.dart';
import 'package:peladas/main.dart';
import 'package:peladas/peladaDetalhe.dart';
import 'package:shared_preferences/shared_preferences.dart';

class ConfiguracaoDetailScreen extends StatefulWidget {
  final Configuracao configuracao;
  ConfiguracaoDetailScreen({this.configuracao});
  @override
  _configuracaoDetailState createState() => _configuracaoDetailState();
  // TODO: implement createState
}

class _configuracaoDetailState extends State<ConfiguracaoDetailScreen> {
  Api api = Api();
  SharedPreferences prefs;
  String _variable;
  _getToken() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    setState(() {
      _variable = (prefs.getString('token')) ?? "";
    });
  }

  _mapTypes() {
    Map<String, String> mymap = new HashMap();
    mymap['O'] = 'Ordem de chegada';
    return mymap;
  }

  _mapTempos() {
    Map<String, String> mymap = new HashMap();
    mymap['T1'] = 'Apenas um tempo';
    mymap['T2'] = 'Dois tempos';
    return mymap;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        actions: <Widget>[
          IconButton(
            icon: Icon(Icons.edit),
            color: Colors.red,
            onPressed: () {
              _getToken();
              Navigator.push(
                context,
                MaterialPageRoute(
                    builder: (context) => EditConfiguracaoScreen(
                        configuracao: widget.configuracao,
                        id: widget.configuracao.id,
                        token: _variable)),
              );
            },
          ),
        ],
        backgroundColor: Colors.white,
        title: Center(
          child: Text("Configuração",
              style: new TextStyle(
                  color: Colors.red, fontWeight: FontWeight.normal)),
        ),
        automaticallyImplyLeading: false,
      ),
      body: new Container(
        child: Column(
          children: <Widget>[
            Card(
                child: ListTile(
              title: Text("Duração de cada partida"),
              subtitle: Text(widget.configuracao.tempo_duracao),
            )),
            Card(
                child: ListTile(
              title: Text("Quantidade de jogadores por equipe"),
              subtitle: Text(widget.configuracao.qtd_jogadores),
            )),
            Card(
                child: ListTile(
              title: Text("Tipo de sorteio"),
              subtitle: Text(_mapTypes()["O"]),
            )),
            Card(
                child: ListTile(
                    title: Text("Limite de Gols por partida"),
                    subtitle: Text(widget.configuracao.limite_gols))),
            Card(
                child: ListTile(
                    title: Text("Tempos por partida"),
                    subtitle: Text(_mapTempos()[widget.configuracao.tempos])))
          ],
        ),
      ),
    );
  }
}
