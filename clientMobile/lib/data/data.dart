class Token {
  String token;
  Token({this.token});
}

class Pelada {
  var id;
  var nome;
  Configuracao configuracao;
  var dono;
  Pelada({this.id, this.nome, this.configuracao, this.dono});
}

class Dono {
  String username;
  String email;
  Dono({this.username, this.email});
}

class User {
  int id;
  String username;
  String email;
  User({this.username, this.email, this.id});
}

class Jogador {
  int id;
  String nome;
  String phone;
  String email;
  int rating;
  Jogador({
    this.id,
    this.nome,
    this.rating,
    this.email,
  });
}

class PeladaDetalhe {
  int id;
  String nome;
  Dono dono;
  List<Jogador> jogadores;
  PeladaDetalhe({
    this.id,
    this.nome,
    this.dono,
    this.jogadores,
  });
}

class Configuracao {
  var id;
  var tempos;
  var tempo_duracao;
  var limite_gols;
  var qtd_jogadores;
  var tipo_sorteio;
  Configuracao(
      {this.tempos,
      this.tempo_duracao,
      this.id,
      this.limite_gols,
      this.qtd_jogadores,
      this.tipo_sorteio});
}
