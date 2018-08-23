import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:peladas/add_jogador.dart';
import 'package:peladas/data/data.dart';
import 'package:peladas/main.dart';
import 'package:peladas/star.dart';
import 'package:shared_preferences/shared_preferences.dart';

class JogadoresScreen extends StatefulWidget {
  PeladaDetalhe pelada;
  JogadoresScreen({this.pelada});
  @override
  _jogadoresState createState() => _jogadoresState();
  // TODO: implement createState
}

class _jogadoresState extends State<JogadoresScreen> {
  Api api = Api();
  SharedPreferences prefs;
  String _variable;

  void _callDelete() async {
    // final result = await new Api().postJogador(id, rating, pelada, token);
  }
  _getToken() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    setState(() {
      _variable = (prefs.getString('token')) ?? "";
    });
  }

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();
    return Scaffold(
      floatingActionButton: FloatingActionButton(
          onPressed: () {
            _getToken();
            Navigator.push(
              context,
              MaterialPageRoute(
                  builder: (context) =>
                      AddJogador(id: widget.pelada.id, token: _variable)),
            );
          },
          backgroundColor: Colors.red,
          child: Icon(
            Icons.add,
            color: Colors.white,
          )),
      appBar: AppBar(
        backgroundColor: Colors.white,
        title: Center(
          child: Text(widget.pelada.nome,
              style: new TextStyle(
                  color: Colors.red, fontWeight: FontWeight.normal)),
        ),
        actions: <Widget>[
          IconButton(
            icon: Icon(Icons.people_outline),
            color: Colors.red,
            onPressed: () {
              _getToken();
              Navigator.push(
                context,
                MaterialPageRoute(
                    builder: (context) =>
                        AddJogador(id: widget.pelada.id, token: _variable)),
              );
            },
          ),
        ],
        automaticallyImplyLeading: false,
      ),
      body: new Container(
          child: new ListView.builder(
        itemCount: widget.pelada.jogadores.length,
        itemBuilder: (context, index) {
          var jogador = widget.pelada.jogadores[index];
          // var email = jogador?.email ?? "null@null.com";

          return Column(
            children: <Widget>[
              new Card(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: <Widget>[
                    Container(
                        padding: const EdgeInsets.only(bottom: 8.0),
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          crossAxisAlignment: CrossAxisAlignment.center,
                          children: <Widget>[
                            Padding(
                              padding:
                                  const EdgeInsets.only(top: 8.0, left: 8.0),
                              child: Text(jogador.nome),
                            ),
                            // Padding(
                            //   padding:
                            //       const EdgeInsets.only(top: 8.0, right: 8.0),
                            //   child: InkWell(
                            //       onTap: () {
                            //         _getToken();
                            //         Scaffold.of(context)
                            //             .showSnackBar(new SnackBar(
                            //           content: Text(this._variable),
                            //         ));
                            //       },
                            //       child: Icon(Icons.delete)),
                            // ),
                          ],
                        )),
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: StarRating(
                        color: Colors.red,
                        rating:
                            widget.pelada.jogadores[index].rating.toDouble(),
                      ),
                    )
                  ],
                ),
              ),
            ],
          );
        },
      )),
    );
  }
}
