int a = 2;
int b = 3;
int c = 4;
int d = 5;
int e = 6;
int f = 9;
int g = 8;

int led_naranja = 10;
int led_rojo = 11;
int led_verde = 12;
int led_azul = 13;

int contador = 0;
int estado = 0; // 0: Inactivo, 1: Verde, 2: Naranja, 3: Rojo, 4: Azul
unsigned long tiempoAzul = 0;

void apagarDisplay() {
  digitalWrite(a, LOW);
  digitalWrite(b, LOW);
  digitalWrite(c, LOW);
  digitalWrite(d, LOW);
  digitalWrite(e, LOW);
  digitalWrite(f, LOW);
  digitalWrite(g, LOW);
}

void mostrarNumero(int numero) {
  digitalWrite(a, (numero == 0 || numero == 2 || numero == 3 || numero == 5 || numero == 6 || numero == 7 || numero == 8 || numero == 9) ? HIGH : LOW);
  digitalWrite(b, (numero == 0 || numero == 1 || numero == 2 || numero == 3 || numero == 4 || numero == 7 || numero == 8 || numero == 9) ? HIGH : LOW);
  digitalWrite(c, (numero == 0 || numero == 1 || numero == 3 || numero == 4 || numero == 5 || numero == 6 || numero == 7 || numero == 8 || numero == 9) ? HIGH : LOW);
  digitalWrite(d, (numero == 0 || numero == 2 || numero == 3 || numero == 5 || numero == 6 || numero == 8 || numero == 9) ? HIGH : LOW);
  digitalWrite(e, (numero == 0 || numero == 2 || numero == 6 || numero == 8) ? HIGH : LOW);
  digitalWrite(f, (numero == 0 || numero == 4 || numero == 5 || numero == 6 || numero == 8 || numero == 9) ? HIGH : LOW);
  digitalWrite(g, (numero == 2 || numero == 3 || numero == 4 || numero == 5 || numero == 6 || numero == 8 || numero == 9) ? HIGH : LOW);
}

void setup() {
  // Configurar pines como salida
  pinMode(a, OUTPUT);
  pinMode(b, OUTPUT);
  pinMode(c, OUTPUT);
  pinMode(d, OUTPUT);
  pinMode(e, OUTPUT);
  pinMode(f, OUTPUT);
  pinMode(g, OUTPUT);

  pinMode(led_naranja, OUTPUT);
  pinMode(led_rojo, OUTPUT);
  pinMode(led_verde, OUTPUT);
  pinMode(led_azul, OUTPUT);

  // Inicializar el monitor serie
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    int numero = Serial.parseInt();
    
    switch (numero) {
      case 1:
        estado = 1; // Verde
        contador = 0;
        break;
      case 2:
        estado = 0; // Inactivo
        digitalWrite(led_naranja, LOW);
        digitalWrite(led_rojo, LOW);
        digitalWrite(led_verde, LOW);
        digitalWrite(led_azul, LOW);
        apagarDisplay(); // Apagar el display al enviar el número 2
        break;
      case 3:
        estado = 4; // Azul
        digitalWrite(led_azul, HIGH);
        tiempoAzul = millis(); // Guardar el tiempo actual para el LED azul
        break;
    }
  }

  switch (estado) {
    case 1: // Verde
      digitalWrite(led_naranja, LOW);
      digitalWrite(led_rojo, LOW);
      digitalWrite(led_verde, HIGH);

      mostrarNumero(contador);

      delay(1000);

      contador++;

      if (contador > 9) {
        contador = 0;
        digitalWrite(led_verde, LOW); // Apagar el LED verde al llegar a 9
        estado = 2; // Cambiar a estado naranja
      }
      break;

    case 2: // Naranja
      digitalWrite(led_verde, LOW);
      digitalWrite(led_rojo, LOW);
      digitalWrite(led_naranja, HIGH);

      mostrarNumero(contador);

      delay(1000);

      contador++;

      if (contador > 5) {
        contador = 0;
        estado = 3; // Cambiar a estado rojo
      }
      break;

    case 3: // Rojo
      digitalWrite(led_naranja, LOW);
      digitalWrite(led_verde, LOW);
      digitalWrite(led_rojo, HIGH);

      mostrarNumero(9 - contador); // Contar de 9 a 0

      delay(1000);

      contador++;

      if (contador > 9) {
        contador = 0;
        estado = 1; // Volver a estado verde
      }
      break;

    case 4: // Azul
      digitalWrite(led_naranja, LOW);
      digitalWrite(led_rojo, LOW);
      digitalWrite(led_verde, LOW);

      // El LED azul permanece encendido durante 15 segundos
      if (millis() - tiempoAzul > 15000) {
        digitalWrite(led_azul, LOW);
        estado = 5; // Cambiar a estado apagar azul
      }
      break;

    case 5: // Apagar azul
      // Realizar acciones de apagado, si es necesario
      delay(1000);
      estado = 2; // Volver a estado naranja después de apagar azul
      break;
  }
}

