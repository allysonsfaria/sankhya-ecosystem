---
id: "42427252165271"
titulo: "Entenda tudo sobre o Reconhecimento Facial e cadastro de Biometrias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427252165271-Entenda-tudo-sobre-o-Reconhecimento-Facial-e-cadastro-de-Biometrias"
trilha: "PONTOTEL: Sistema de marcação de ponto > Gestão"
atualizado_em: "2026-08-03T13:29:57Z"
rotulos: ["sync_hc", "pontotel", "pontotel_6a332850ae39c0b9a3cedd0a", "sync_hash_e7cb896bca02"]
---

# Entenda tudo sobre o Reconhecimento Facial e cadastro de Biometrias

O reconhecimento facial é uma funcionalidade de segurança da Pontotel que valida a identidade do colaborador durante o registro de ponto por meio da comparação entre a foto capturada no momento da marcação e as biometrias armazenadas no sistema.
Esse processo aumenta a confiabilidade dos registros, reduz riscos de fraudes e garante mais segurança para a gestão da jornada.

> ⚠️ Atenção: O reconhecimento facial faz parte do módulo Redução de Riscos no Registro. Caso sua empresa ainda não possua esse módulo contratado, entre em contato com nossa equipe para conhecer a solução.

---

## Como habilitar o reconhecimento facial

Para utilizar o reconhecimento facial, é necessário configurar um perfil de coletor com as opções de validação facial habilitadas.

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), abra o menu Admin e clique na opção Coletores\*.
2. Selecione a aba **Perfil de coletores**.

   ![Imagem 1: Selecione a aba Perfil de coletores .](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1i15vvx.png)
3. Escolha a **categoria** desejada:

   - **Dispositivo para registro via web**: utilizado no site BatePonto.
   - **Aplicativo de registro**: utilizado no aplicativo BatePonto.
   - **Aplicativo Gestão**: utilizado no aplicativo Pontotel Gestão.

   ![Imagem 2: Aplicativo Gestão : utilizado no aplicativo Pontotel Gestão.](https://storage.crisp.chat/users/helpdesk/website/-/2/7/e/c/27ec3cacef6d4800/2126385d-09ca-4446-b672-dfe612_k5pyyf.png)
4. **Crie** ou **edite** um perfil de coletor

   - Para editar um perfil já existente, selecione-o na lista e, no menu que abrirá, clique no ícone de lápis para editar.
   - Para criar um novo perfil, clique no botão **criar novo perfil de coletor**

   ![Imagem 3: Para criar um novo perfil, clique no botão criar novo perfil de coletor](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1pyaavw.png)
5. Nas configurações do perfil de coletor, siga os passos abaixo:

   - Acesse a aba **opções de foto**.
   - Ative a opção **detecção facial**.
   - Ative a opção **reconhecimento facial**.
   - Defina a **porcentagem mínima de precisão** para validar o reconhecimento (o padrão recomendado pela Pontotel é **99,2%**).
   - (Opcional) Ative a opção **Detecção de vida (liveness)**. Essa configuração garante que o registro seja feito apenas com rostos reais, evitando tentativas de fraude com fotos ou vídeos.
   - (Opcional) Ative a opção **Iniciar fluxo de ponto pelo reconhecimento facial**. Com ela, o sistema tenta identificar o colaborador automaticamente antes da digitação do PIN.
   - **Se o rosto for reconhecido:** os dados do colaborador aparecerão para confirmação.
   - **Se não houver reconhecimento:** o colaborador deverá digitar o PIN normalmente.
   - **Se a opção estiver desabilitada:** o colaborador digitará o PIN primeiro, e só depois será feita a validação com a câmera.

   ![Exemplo de preenchimento de um perfil para o reconhecimento facial](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_l6xllm.png)

   Exemplo de preenchimento de um perfil para o reconhecimento facial
6. Clique em **Salvar** ou **Criar perfil**.

---

## Como aplicar o perfil nos coletores

Após criar o perfil, é necessário vinculá-lo aos coletores que realizarão o registro de ponto.

1. Acesse **Admin > Coletores**.
2. Selecione a categoria desejada.
3. Localize o coletor.
4. Clique em editar.
5. No campo **Perfil de coletor**, selecione o perfil criado com reconhecimento facial habilitado.
6. Salve as alterações.

[GIF animado: Imagem 5: Salve as alterações.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/trocar-perfil-de-coletor_rq8kxa.gif)

> 💡 Dica: Para novos coletores, o perfil pode ser selecionado já durante a configuração inicial do dispositivo.

---

## Como habilitar a câmera para os colaboradores

Além da configuração dos coletores, o colaborador também precisa estar autorizado a utilizar a câmera durante o registro.

1. Acesse **Cadastros > Empregados**.
2. Selecione o colaborador desejado.
3. Clique em **editar**.
4. Acesse a seção **Config. de ponto e benefícios**.
5. Habilite as opções relacionadas ao uso da câmera e reconhecimento facial.

![Imagem 6: Habilite as opções relacionadas ao uso da câmera e reconhecimento facial.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1s2wkht.png)

---

## Gestão de biometria facial

A Gestão de Biometria Facial é o local onde ficam armazenadas todas as fotos utilizadas pelo reconhecimento facial.
É nessa área que você pode:

- Visualizar biometrias cadastradas.
- Aprovar ou desaprovar fotos.
- Consultar registros existentes.
- Atualizar biometrias dos colaboradores.
- Garantir que o reconhecimento facial possua imagens de qualidade para comparação.

### Como acessar

Existem duas formas de acessar a gestão de biometria.

**Opção 1:**

1. Acesse **Cadastros > Empregados**.
2. Selecione o colaborador.
3. Clique em editar.
4. Acesse **Config. de ponto e benefícios**.
5. Abra a aba **Biometria facial**.

**Opção 2:**

1. Acesse **Cadastros > Biometria Facial**.
2. Utilize os filtros para localizar colaboradores específicos.

![Imagem 7: Utilize os filtros para localizar colaboradores específicos.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_2abh7g.png)

### O que são as fotos aprovadas?

As fotos aprovadas são as imagens utilizadas como referência pelo reconhecimento facial.
Quando um colaborador realiza um registro de ponto, a foto capturada é comparada com essas imagens para confirmar sua identidade.
Cada colaborador pode possuir até cinco biometrias ativas.
Quanto melhor a qualidade dessas imagens, maior será a precisão do reconhecimento facial.
Por isso, recomendamos manter sempre as cinco biometrias atualizadas, contemplando possíveis mudanças de aparência, como:

- Uso ou remoção de barba.
- Utilização de óculos.
- Mudanças de corte de cabelo.
- Diferentes condições de iluminação.

### Boas práticas para fotos de reconhecimento facial

A qualidade das imagens influencia diretamente no desempenho da tecnologia.

**Fotos recomendadas:**
✅ Rosto centralizado e voltado para a câmera.
✅ Boa iluminação.
✅ Fundo neutro.
✅ Apenas uma pessoa na imagem.
✅ Rosto totalmente visível.
✅ Foto nítida e sem movimentação.

![Imagem 8: Fotos recomendadas: ✅ Rosto centralizado e voltado para a câmera. ✅ Boa iluminação. ✅ Fundo neutro. ✅ Apenas uma pessoa…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_xsipt7.png)

**Fotos que devem ser evitadas:**
❌ Fotos escuras ou com excesso de luz.
❌ Imagens desfocadas.
❌ Rosto cortado.
❌ Fotos com múltiplas pessoas.
❌ Uso de filtros.
❌ Óculos escuros, máscaras ou bonés.
❌ Enquadramentos laterais ou inclinados.

![Imagem 9: Fotos que devem ser evitadas: ❌ Fotos escuras ou com excesso de luz. ❌ Imagens desfocadas. ❌ Rosto cortado. ❌ Fotos com…](https://storage.crisp.chat/users/helpdesk/website/-/5/2/7/4/527462fcc09b8c00/d20db10d-d596-4a9d-873b-9f0f39_fjr0pv.png)
> 💡 Dica: [Neste artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427309338135) você verá um passo a passo para visualizar a foto associada diretamente aos dados do registro de ponto na **folha de ponto do colaborador**.

---

## ✨ Novidade: Cadastro de Biometria Fácil

Além das biometrias geradas a partir dos registros de ponto, a Pontotel também disponibiliza o **Cadastro de Biometria Fácil**.
Essa funcionalidade permite realizar um cadastro da biometria do colaborador diretamente pelo celular, garantindo imagens de alta qualidade para o reconhecimento facial.

### Quando utilizar

O Cadastro de Biometria Fácil é recomendado principalmente para:

- Novos colaboradores.
- Correção de biometrias com baixa qualidade.
- Casos de falhas recorrentes no reconhecimento facial.
- Atualização de fotos antigas.

### Como funciona

O processo é realizado em um fluxo guiado e validado em tempo real.
Primeiro, é informado o PIN do colaborador.
Em seguida, os dados do funcionário são exibidos para conferência, reduzindo o risco de associar a biometria à pessoa errada.
Após a confirmação, o sistema abre a câmera do dispositivo e passa a orientar a captura da foto.
Durante esse processo, mensagens podem ser exibidas automaticamente, como:

- Chegue mais perto.
- Afaste um pouco.
- Olhe para a câmera.
- Deixe a cabeça reta.
- Precisa de mais luz.
- Evite luz direta.
- Fique parado.
  A captura somente é liberada quando todos os critérios mínimos de qualidade forem atendidos.

![Imagem 10: Fique parado. A captura somente é liberada quando todos os critérios mínimos de qualidade forem atendidos.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/download_fxwztl.svg)

### Validação automática da qualidade

Antes de aprovar uma biometria, o sistema analisa automaticamente:

- Presença de apenas uma pessoa na imagem.
- Enquadramento adequado.
- Distância correta da câmera.
- Boa iluminação.
- Nitidez da foto.
- Posicionamento correto do rosto.
  Somente após a aprovação desses critérios a biometria é cadastrada.

### Substituição de biometrias

Quando o colaborador já possui cinco biometrias ativas, o sistema permite substituir automaticamente a biometria mais antiga.
O histórico das imagens anteriores é mantido para auditoria e rastreabilidade.

### Como acessar

O Cadastro de Biometria Fácil está disponível exclusivamente para dispositivos móveis.
Atualmente, ele não possui acesso pelo menu do site Gestão, nem pelos aplicativos.

O acesso deve ser realizado pelo navegador do smartphone, através do link: [<https://gestao.pontotel.com.br/#/biometria/autenticar](https://gestao.pontotel.com.br/#/biometria/autenticar>)

> ⚠️ Importante: A funcionalidade é controlada por uma liberação específica. Caso tenha interesse em utilizar o recurso, entre em contato com o time de Suporte para solicitar a habilitação.

---

O reconhecimento facial da Pontotel oferece uma camada adicional de segurança para os registros de ponto, reduzindo inconsistências e aumentando a confiabilidade das marcações.
Ao manter as biometrias atualizadas e utilizar recursos como o Cadastro de Biometria Fácil, sua empresa garante uma base biométrica mais confiável, melhora a taxa de reconhecimento e proporciona uma experiência mais segura para colaboradores, gestores e equipes de RH.

Caso tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao[site Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo[WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
