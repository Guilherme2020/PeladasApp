import 'dart:async';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:peladas/configuracao_details.dart';
import 'package:peladas/data/data.dart';
import 'package:peladas/main.dart';
import 'package:peladas/peladaDetalhe.dart';
import 'package:peladas/star.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:http/http.dart' as http;

class AddJogador extends StatefulWidget {
  final int id;
  final String token;
  AddJogador({this.id, this.token});
  @override
  _AddJogadorState createState() => _AddJogadorState();
}

class _AddJogadorState extends State<AddJogador> {
  final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();
  Api api = Api();
  SharedPreferences prefs;
  final nome = TextEditingController();
  double rating = 3.0;
  int _rating = 0;

  _callSubmit(String nome, int rating, String pelada, String token) async {
    final result = await new Api().postJogador(nome, rating, pelada, token);
    _scaffoldKey.currentState.showSnackBar(
      SnackBar(
        content: Text(
          result.toString(),
        ),
      ),
    );
    if (result.toString() == 'true') {
      Navigator.of(context).pop();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        key: _scaffoldKey,
        appBar: AppBar(
          backgroundColor: Colors.white,
          title: Center(
            child: Text(
              "Adicionar Jogador",
              style: TextStyle(
                color: Colors.red,
                fontWeight: FontWeight.normal,
              ),
            ),
          ),
          automaticallyImplyLeading: false,
        ),
        body: Column(
          children: <Widget>[
            Padding(
              padding: EdgeInsets.all(16.0),
              child: TextFormField(
                decoration: InputDecoration(
                  labelText: 'Nome',
                  fillColor: Colors.red,
                  labelStyle: TextStyle(color: Colors.red),
                  hintStyle: TextStyle(
                    color: Colors.red,
                  ),
                ),
                controller: nome,
              ),
            ),
            Padding(
              padding: EdgeInsets.all(16.0),
              child: StarRating(
                rating: this.rating,
                onRatingChanged: (rating) =>
                    setState(() => this.rating = rating),
              ),
            ),
            SizedBox(
              width: double.infinity,
              child: Padding(
                padding: const EdgeInsets.all(8.0),
                child: FlatButton(
                  color: Colors.red,
                  onPressed: () {
                    _callSubmit(nome.text, this.rating.toInt(),
                        widget.id.toString(), widget.token);
                  },
                  child: Text(
                    'Salvar',
                    style: new TextStyle(
                      color: Colors.white,
                      fontFamily: 'Heavy',
                    ),
                  ),
                ),
              ),
            ),
          ],
        ));
  }
}
