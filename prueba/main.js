
console.log('Holiiss');
let globalId = null;
let logok = 0;
let flag_ev = false;
let stdata;
let tmm;
let stm;
var date;
var indx = ["1", "2", "3", "4", "5", "6"];
var indx = ["ent1", "ent2", "ent3", "ent4", "ent5", "ent6", "sal1", "sal2"];
const signupForm = document.querySelector('#singup-form');
const signinForm = document.querySelector('#login-form');
const forgetForm = document.querySelector('#forget-password');


forgetForm.addEventListener('submit', (e) => {
  e.preventDefault();
  //const email = document.querySelector('#singup-email').value;
  //const password = document.querySelector('#singup-password').value;
  //alert("Usted es un tonto que se olvido la contraseña");
  const user = firebase.auth().currentUser;
  //alert("antes de funcion");
  var emailAddress = document.querySelector('#login-password-new').value;//"654321";
  //alert("despues de funcion");

  // user.updatePassword(newPassword).then(() => {
  //   // Update successful.
  //   alert("su password fue cambiado");
  // }).catch((error) => {
  //   alert("Error: su password no pudo cambiarse");
  //   // An error ocurred
  //   // ...
  // });

  var auth = firebase.auth();
  //var emailAddress = "cristianj_al@hotmail.com";

  auth.sendPasswordResetEmail(emailAddress).then(function () {
    // Email sent.
    console.log('Email Sent');
  }).catch(function (error) {
    // An error happened.
  });


})

signupForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const email = document.querySelector('#singup-email').value;
  const password = document.querySelector('#singup-password').value;
  console.log(email, password)
  auth
    .createUserWithEmailAndPassword(email, password)
    .then(userCredential => {
      console.log("El usuario ha sido creado");
      var user = userCredential.user
      console.log("el usuario es ${user}");
      signupForm.reset();
      $('#singupModal').modal('hide')


    })
})


signinForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const email = document.querySelector('#login-email').value;
  const password = document.querySelector('#login-password').value;
  console.log(email, password)
  auth
    .signInWithEmailAndPassword(email, password)
    .then(userCredential => {
      console.log("El usuario ha sido chequeado");
      signinForm.reset();
      var user = userCredential.user
      console.log("el usuario es ");
      console.log(user);
      let userId = user.uid;
      globalId = userId;
      console.log("y su uid es ");
      console.log(userId);
      flag_ev = true;
      tmm = Date.now();
      console.log("el tiempo es");
      console.log(tmm);
      //db
      // .ref('users/' + userId).set({
      //   username: "holiss soy cristian 222",
      //   email: "myemail@user.com",

      // });
      // .ref('users/' + userId + '/valdig').set({
      //   ent1:{
      //   val: "ON",
      //   nom: "flotador1",
      //   time: tmm.toString(),
      //   },
      //   ent2:{
      //   val: "OFF",
      //   nom: "flotador2",
      //   time: tmm.toString(),
      //   },
      //   ent3:{
      //   val: "OFF",
      //   nom: "flotador3",
      //   time: tmm.toString(),
      //   },
      //   ent4:{
      //   val: "ON",
      //   nom: "llave1",
      //   time: tmm.toString(),
      //   },
      //   ent5:{
      //   val: "ON",
      //   nom: "llave2",
      //   time: tmm.toString(),
      //   },
      //   ent6:{
      //   val: "OFF",
      //   nom: "llave3",
      //   time: tmm.toString(),
      //   },
      //   sal1:{
      //   val: "ON",
      //   nom: "motor1",
      //   time: tmm.toString(),
      //   },
      //   sal2:{
      //   val: "OFF",
      //   nom: "motor2",
      //   time: tmm.toString(),
      //   }

      // });
      //db
      // .ref('users/' + userId).set({
      //   username: "holiss soy cristian 222",
      //   email: "myemail@user.com",

      // });

      //setea un valor (lo sobrescribe)

      //tmm= Date.now();
      // .ref('users/' + userId + '/valanalog').set({

      //   valanalog7:{ 
      //   val:"10.0",

      //   time: tmm.toString(),
      //   }

      // });

      //Agrega valores (añade un nuevo valor , no elimina los datos anteriores)
      //  tmmm=tmm.toString();
      //  var valanalog2={
      //      val:"15.0",
      //      time:tmmm,
      //  }
      //  var updates ={} ;
      //  updates['users/' + userId + '/valanalog' + '/valanalog_'+tmm] = valanalog2;
      //  firebase.database().ref().update(updates);




      $('#singinModal').modal('hide')


    })
})

// Logout
const logout = document.querySelector("#logout");

logout.addEventListener("click", (e) => {
  e.preventDefault();
  console.log("estoy en logout")
  auth.signOut().then(() => {
    console.log("signup out");
  });
});

// Posts
const postList = document.querySelector(".posts");
const setupPosts = (data) => {
  console.log("estoy tratando de mostrar el dato");
  console.log(data);
  console.log(data.email);
  console.log(data.username);
  if (data.length) {
    let html = "";

    //const post = data;
    const li = `
      <li class="list-group-item list-group-item-action">
        <h5>${data.email}</h5>
        <p>${data.username}</p>
      </li>
    `;


    postList.innerHTML = html;
  } else {
    //postList.innerHTML = '<h4 class="text-white">Login to See Posts</h4>';
  }
};

//events
//list for auth state changes
// auth.onAuthStateChanged((user) => {
//   if (user) {
//     console.log("signin");
//     db.collection("users")
//       .get()
//       .then((snapshot) => {
//         setupPosts(snapshot.docs);
//         loginCheck(user);
//       });
//   } else {
//     console.log("signout");
//     setupPosts([]);
//     loginCheck(user);
//   }
// });

auth.onAuthStateChanged((user) => {
  if (user) {

    db.ref("users/" + globalId + "/tabla").on('value', function (snapshot) {
      var dato = snapshot.val();
      console.log("El dato leido es");
      console.log(dato);
      let i = 0;
      snapshot.forEach(function (childSnapshot) {
        // key will be "ada" the first time and "alan" the second time
        var key = childSnapshot.key;
        // childData will be the actual contents of the child
        var childata = childSnapshot.val();
        console.log("estamos probando la indexacion");
        console.log(indx[i] + "Id")
        console.log(childata.nom);
        console.log(childata.val);
        var nom = document.getElementById(indx[i] + "Id");
        var val = document.getElementById(indx[i] + "val");

        nom.innerHTML = childata.nom;
        val.innerHTML = childata.val;
        //document.getElementById("ent"+indx[i]+"Id").innerHTML = childata.nom;
        //document.getElementById("ent"+indx[i]+"val").innerHTML = childata.val;
        date = parseInt(childata.time, 10);
        date = new Date(date);
        document.getElementById(indx[i] + "time").innerHTML = date;
        if (childata.val == true) {
          document.getElementById(indx[i] + "val").className = "active";
        }
        else {
          document.getElementById(indx[i] + "val").className = "waiting";
        }

        i++;
        console.log(i);
        //console.log(dato.entrada1_nom);

        // console.log(dato.entrada1_nom);
        // console.log(dato.entrada1_val);
        // document.getElementById("ent1Id").innerHTML = dato.entrada1_nom;
        // document.getElementById("ent1val").innerHTML = dato.entrada1_val;
        // date = parseInt(dato.time1,10);
        // date = new Date(date);
        // document.getElementById("ent1time").innerHTML = date;
        // if(dato.entrada1_val == "ON"){
        //   document.getElementById("ent1val").className ="active";
        // }
        // else{
        //   document.getElementById("ent1val").className ="waiting";
        // }
      });


      //setupPosts(dato);
    });


    // PPIO-obtiene todo el dato del usuario UID
    db.ref('users').child(globalId).child("valanalog").on('value', function (snapshot) {
      var dato2 = snapshot.val();
      console.log("leyendo un valor analogico");
      // console.log(dato2.valanalog1.time);
      // console.log(dato2.valanalog1.val);
      // var recentPostsRef = db.ref('users/'+globalId+'valanalog').limitToLast(3);
      // console.log("leyendo los ultimos 3 valores");
      // console.log(recentPostsRef);

    });
    // FIN-obtiene todo el dato del usuario UID


    // PPIO -- Obtiene los ultimos N valores


    db.ref("users/" + globalId + "/dataHistory").limitToLast(10).on("value", function (snapshot) {
      var dato3 = snapshot.val();
      console.log("leyendo un valor analogico 2do intento");
      console.log(dato3);

      tiempos = [];
      valores = [];

      snapshot.forEach(function (childSnapshot) {
        // key will be "ada" the first time and "alan" the second time
        var key = childSnapshot.key;
        // childData will be the actual contents of the child
        var childData = childSnapshot.val();
        console.log(key);
        console.log("leyendo campo tiempo");
        console.log(childData.time);
        console.log("leyendo  campo valor");
        console.log(childData.analog);


        // Create a new JavaScript Date object based on the timestamp
        var date = new Date(childData.time * 1);
        var day = date.getDate();
        var month = date.getMonth();
        var year = date.getFullYear();
        // Hours part from the timestamp
        var hours = date.getHours();
        // Minutes part from the timestamp
        var minutes = "0" + date.getMinutes();
        // Seconds part from the timestamp
        var seconds = "0" + date.getSeconds();

        // Will display time in 10:30:23 format
        var formattedTime = day + "/" + month + "/" + year + " " + hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
        console.log("fecha");
        console.log(formattedTime);

        tiempos.push(formattedTime);
        valores.push(childData.analog);






      });


      console.log("Los datos de tiempo de los ultimos N valores");
      console.log(tiempos);
      console.log("Los datos de valores de los ultimos N valores");
      console.log(valores);

      var data = [{
        //x: [1999, 2000, 2001, 2002],
        x: tiempos,
        y: valores,
        type: 'scatter',
        mode: 'lines',
        name: '2000'
        // line: {
        //   color: 'rgb(0, 128, 0)',
        //   width: 2
        // }
      }];

      var layout = {
        title: 'LOWI-CON',
        xaxis: {
          title: 'tiempo',
          //type: 'date',
          showticklabels : false,
          zeroline: true,
          rangemode: 'tozero',
          //showgrid: false,
          //zeroline: false
        },
        yaxis: {
          title: 'temperatura',
          showline: false
        }
      };

      //import "https://cdn.plot.ly/plotly-2.5.1.min.js"

      Plotly.newPlot("chart1", data, layout);



    });

    // FIN -- Obtiene los ultimos N valores

    // PPIO -- Obtiene un rango de valores
    function toTimestamp(strDate) {
      var datum = Date.parse(strDate);
      return datum / 1000;
    }

    const evgraf = document.querySelector("#graf-form");
    // const t1g = document.querySelector('#t1_graf');
    // const t2g = document.querySelector('#t2_graf');

    evgraf.addEventListener('submit', (e) => {
      e.preventDefault();

      const t1g = document.querySelector('#t1_graf').value;
      const t2g = document.querySelector('#t2_graf').value;
      const t1s = toTimestamp(t1g);
      const t2s = toTimestamp(t2g);
      const t11s = t1s * 1000;
      const t22s = t2s * 1000;
      console.log("intento de captura de tiempo")
      console.log(t1g);
      console.log(t2g);
      console.log(t1s);
      console.log(t2s);
      console.log(t11s);
      console.log(t22s);

      db.ref("users/" + globalId + "/dataHistory").orderByChild("time").startAt(t11s).endAt(t22s).on("value", function (snapshot) {
        var dato4 = snapshot.val();
        console.log("leyendo un rango de datos");
        console.log(dato4);

        tiempos = [];
        valores = [];

        snapshot.forEach(function (childSnapshot) {
          // key will be "ada" the first time and "alan" the second time
          var key = childSnapshot.key;
          // childData will be the actual contents of the child
          var childData = childSnapshot.val();
          console.log(key);
          console.log("leyendo campo tiempo");
          console.log(childData.time);
          console.log("leyendo  campo valor");
          console.log(childData.analog);


          // Create a new JavaScript Date object based on the timestamp
          var date = new Date(childData.time * 1);
          var day = date.getDate();
          var month = date.getMonth();
          var year = date.getFullYear();
          // Hours part from the timestamp
          var hours = date.getHours();
          // Minutes part from the timestamp
          var minutes = "0" + date.getMinutes();
          // Seconds part from the timestamp
          var seconds = "0" + date.getSeconds();

          // Will display time in 10:30:23 format
          var formattedTime = day + "/" + month + "/" + year + " " + hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
          console.log("fecha");
          console.log(formattedTime);

          tiempos.push(formattedTime);
          valores.push(childData.analog);






        });
        console.log("Los datos de tiempo del rango de valores");
        console.log(tiempos);
        console.log("Los datos de valores del rango de valores");
        console.log(valores);

        var data = [{
          //x: [1999, 2000, 2001, 2002],
          x: tiempos,
          y: valores,
          type: 'scatter',
          mode: 'lines',
          name: '2000',
          // line: {
          //   color: 'rgb(0, 128, 0)',
          //   width: 2
          // }
        }];

        var layout = {
          title: 'LOWI-CON',
          xaxis: {
            title: 'tiempo',
            // type: 'date',
            showticklabels : false,
            zeroline: true,
            rangemode: 'tozero',
            //showgrid: false,
            //zeroline: false
          },
          yaxis: {
            title: 'temperatura',
            showline: false
          }
        };

        //import "https://cdn.plot.ly/plotly-2.5.1.min.js"

        Plotly.newPlot("chart2", data, layout);

      });

    });

    // FIN -- Obtiene un rango de valores








    // PPIO --Obtiene los datos ordenados por tiempo

    db.ref("users/" + globalId + "/valanalog").orderByChild("time").on("value", function (snapshot) {
      // var valor = snapshot.val();
      // console.log("datos ordenados");
      // console.log(valor);
      snapshot.forEach(child => {
        console.log(child.key, child.val());
      });

    });

    // FIN --Obtiene los datos ordenados por tiempo

  }

});





