---
id: "42427670675607"
titulo: "Dúvidas frequentes sobre a integração com RD Station"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427670675607-D%C3%BAvidas-frequentes-sobre-a-integra%C3%A7%C3%A3o-com-RD-Station"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:06:45Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452443", "sync_hash_97521dbfb5d8"]
---

# Dúvidas frequentes sobre a integração com RD Station

1. **Ao habilitar a integração na tela de Administração, selecionei a opção "Criar cliente e oportunidade", porém somente o cliente está sendo criado**

[![Imagem 1: Ao habilitar a integração na tela de Administração, selecionei a opção "Criar cliente e oportunidade", porém somente o…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330271/e894e45927eba41b436156b4/image.png-expires%3D1619816400-signature%3D07db3246f4be8a0ed3d9ad4f9270aa6c8068288909099c8422be3b8bdb240e5a?expires=1786536000&signature=7c8aa563d42245843a7025dd49e9a24e9538f8592df05a1cc930f4ae822e888b&req=dyYuFcp%2Bn4ZeFb4V1XW4gYhmqHFloCu58L64C3HZdY0ORi6HJdWTslu2OdLj%0AYSS55zCl5j5wpvHfw0hGnQjmMg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/76713843/0627d7319f2c3a11cb66904a/image.png?expires=1619816400&signature=07db3246f4be8a0ed3d9ad4f9270aa6c8068288909099c8422be3b8bdb240e5a)

**Explicação:** o Ploomes só cria o Negócio caso as duas condições abaixo sejam satisfeitas:

- Isso foi explicitado nas configurações "Criar cliente e oportunidade"
- O Lead foi marcado como Oportunidade no RD Station antes de ser enviado ao Ploomes

Embora você tenha solicitado ao Ploomes para criar a Oportunidade (ou Negócio) quando o Lead vier do RD, o Ploomes somente o fará se o Lead vier marcado do RD como Oportunidade. O que acontece muitas vezes é que o fluxo não esteja configurado devidamente e com isso o Lead é enviado prematuramente ao Ploomes. Por uma questão conceitual e de boas práticas, caso o Lead não esteja marcado como Oportunidade no RD, somente o cliente e contato serão criados no Ploomes. Abaixo está o exemplo de um contato que foi recebido do RD Station e estava com a marcação Oportunidade = false. Neste caso, mesmo que o usuário tenha solicitado, o Negócio não foi criado.

[![Imagem 2: Embora você tenha solicitado ao Ploomes para criar a Oportunidade (ou Negócio) quando o Lead vier do RD, o Ploomes…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330278/6d68af941696af2ceb1cdaf8/image.png-expires%3D1619816400-signature%3De46264b21b7663b268d96d8eaa072fcfb2c112411969b7271f93ff334a532526?expires=1786536000&signature=3b1ea6324a55a557a162530901bf957473d7a20eab3d6db9731940d45f6061d6&req=dyYuFcp%2Bn4ZXFb4V1XW4gSlsF3NiF1TUn%2FtjHARdmZdf%2FPVFqDgO9UT4vvWI%0AQRUvYMU64oBxdzvAZg49BUOGxw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/76714290/e77112a300da768e64da377d/image.png?expires=1619816400&signature=e46264b21b7663b268d96d8eaa072fcfb2c112411969b7271f93ff334a532526)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**2. Por que só são registradas a primeira e a última conversão de um Lead do RD ao criar o contato no Ploomes?
Explicação:** como pode ser visto na documentação oficial do RD Station, somente as informações da primeira e da última conversão são enviadas pela API do RD Station. Neste caso, não existe uma maneira do Ploomes puxar mais informações do que as que são disponibilizadas atualmente. O link abaixo ilustra este cenário:

<https://ajuda.rdstation.com.br/hc/pt-br/articles/201867844-Integra%C3%A7%C3%A3o-customiz%C3%A1vel-com-sistema-pr%C3%B3prio-Webhook->

A RD Station é uma empresa em constante evolução e possivelmente num futuro próximo novas possibilidades sejam disponibilizadas. Um e-mail para o time de suporte do RD pode ajudar nesta missão :)
