import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:peladas/configuracao_details.dart';
import 'package:peladas/data/data.dart';
import 'package:peladas/main.dart';
import 'package:peladas/peladaDetalhe.dart';
import 'package:shared_preferences/shared_preferences.dart';

class EditConfiguracaoScreen extends StatefulWidget {
  final Configuracao configuracao;
  final int id;
  final String token;

  EditConfiguracaoScreen({this.configuracao, this.id, this.token});

  @override
  _EditConfiguracaoState createState() => _EditConfiguracaoState();

  // TODO: implement createState
}

class _EditConfiguracaoState extends State<EditConfiguracaoScreen> {
  final GlobalKey<FormState> _formKey = new GlobalKey<FormState>();
  List<String> _colors = <String>[
    '',
    'T1',
    'T2',
  ];
  var _color = "";
  List<String> _duracoes = <String>[
    '',
    '00:05:00',
    '00:06:00',
    '00:07:00',
    '00:08:00',
    '00:09:00',
  ];
  String _duracao = '';
  List<String> _qtd_jogadores = <String>[
    '',
    '5',
    '6',
    '7',
    '8',
  ];
  String _qtd_jogador = '';
  Api api = Api();
  SharedPreferences prefs;

  initState() {
    _color = widget.configuracao.tempos;
    _qtd_jogador = widget.configuracao.qtd_jogadores;
    _duracao = widget.configuracao.tempo_duracao;
  }

  List<String> _tempos = ['T1', 'T2'];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          iconTheme: Theme.of(context).iconTheme,
          backgroundColor: Colors.white,
          title: Center(
            child: Text("Editar Configuração",
                style: new TextStyle(
                    color: Colors.red, fontWeight: FontWeight.normal)),
          ),
          automaticallyImplyLeading: false,
        ),
        body: new SafeArea(
          top: false,
          bottom: false,
          child: new Form(
            key: _formKey,
            autovalidate: true,
            child: new ListView(
                padding: const EdgeInsets.symmetric(horizontal: 16.0),
                children: <Widget>[
                  new InputDecorator(
                      decoration: const InputDecoration(
                        icon: Padding(
                          padding: const EdgeInsets.only(top: 8.0),
                          child: Padding(
                            padding: const EdgeInsets.only(top: 8.0),
                            child: const Icon(Icons.hourglass_full),
                          ),
                        ),
                        labelText: 'Tempos',
                      ),
                      // isEmpty: ;_color == widget.configuracao.tempos,
                      child: new DropdownButtonHideUnderline(
                          child: new DropdownButton<String>(
                        value: _color,
                        isDense: true,
                        onChanged: (String newValue) {
                          setState(() {
                            _color = newValue;
                            print(_color);
                          });
                        },
                        items: _colors.map((String value) {
                          return new DropdownMenuItem<String>(
                            value: value,
                            child: new Text(value),
                          );
                        }).toList(),
                      ))),
                  new InputDecorator(
                      decoration: const InputDecoration(
                        icon: Padding(
                          padding: const EdgeInsets.only(top: 8.0),
                          child: Padding(
                            padding: const EdgeInsets.only(top: 8.0),
                            child: const Icon(Icons.hourglass_empty),
                          ),
                        ),
                        labelText: 'Duração da partida',
                      ),
                      // isEmpty: _duracao == widget.configuracao.tempo_duracao,
                      child: new DropdownButtonHideUnderline(
                          child: new DropdownButton<String>(
                        value: _duracao,
                        isDense: true,
                        onChanged: (String newValue) {
                          setState(() {
                            _duracao = newValue;
                          });
                        },
                        items: _duracoes.map((String value) {
                          return new DropdownMenuItem<String>(
                            value: value,
                            child: new Text(value),
                          );
                        }).toList(),
                      ))),
                  new InputDecorator(
                      decoration: const InputDecoration(
                        icon: Padding(
                          padding: const EdgeInsets.only(top: 8.0),
                          child: const Icon(Icons.person_outline),
                        ),
                        labelText: 'Quantidade de Jogadores por time',
                      ),
                      // isEmpty:
                      //     _qtd_jogador == widget.configuracao.qtd_jogadores,
                      child: new DropdownButtonHideUnderline(
                          child: new DropdownButton<String>(
                        value: _qtd_jogador,
                        isDense: true,
                        onChanged: (String newValue) {
                          setState(() {
                            _qtd_jogador = newValue;
                          });
                        },
                        items: _qtd_jogadores.map((String value) {
                          return new DropdownMenuItem<String>(
                            value: value,
                            child: new Text(value),
                          );
                        }).toList(),
                      ))),
                ]),
          ),
        ));
  }
}
