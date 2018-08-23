import 'dart:collection';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:peladas/add_pelada.dart';
import 'package:peladas/data/data.dart';
import 'package:peladas/main.dart';
import 'package:peladas/peladaDetalhe.dart';
import 'package:shared_preferences/shared_preferences.dart';

class PrincipalScreen extends StatefulWidget {
  final User user;
  PrincipalScreen({this.user});
  @override
  _principalState createState() => _principalState();
}

class _principalState extends State<PrincipalScreen> {
  Api api = Api();
  String _token;

  _getValues() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();

    setState(() {
      _token = (prefs.getString('token')) ?? "";
    });
  }

  @override
  void initState() {
    _getValues();

    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.white,
        title: Center(
          child: Text("Bem vindo , " + widget.user.username,
              style: new TextStyle(
                  color: Colors.red, fontWeight: FontWeight.normal)),
        ),
        automaticallyImplyLeading: false,
      ),
      body: new Container(
          child: new FutureBuilder<List<Pelada>>(
        future: api.userPeladas(_token),
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return new ListView.builder(
                itemCount: snapshot.data.length,
                itemBuilder: (context, index) {
                  return FutureBuilder<PeladaDetalhe>(
                    future: api.peladaDetalhe(_token, snapshot.data[index].id),
                    builder: (context, detalhe) => Column(
                          children: <Widget>[
                            new InkWell(
                              onTap: () {
                                Navigator.push(
                                  context,
                                  CupertinoPageRoute(
                                      builder: (context) => detalhes(
                                            id: snapshot.data[index].id,
                                            token: _token,
                                          )),
                                );
                              },
                              child: new Card(
                                  child: new Column(
                                mainAxisSize: MainAxisSize.min,
                                children: <Widget>[
                                  ListTile(
                                    title: Text(detalhe.data.nome),
                                  )
                                ],
                              )),
                            ),
                          ],
                        ),
                  );
                });
          } else if (snapshot.hasError) {
            return new Text("${snapshot.error}");
          }

          // By default, show a loading spinner
          return new CircularProgressIndicator();
        },
      )),
    );
  }
}
