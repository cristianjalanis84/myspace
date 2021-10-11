console.log('Holiiss');
let globalId =null;
let logok = 0;
let flag_ev=false;
let stdata ;
const signupForm = document.querySelector('#singup-form');
const signinForm = document.querySelector('#login-form');

signupForm.addEventListener('submit',(e) => {
    e.preventDefault();
    const email = document.querySelector('#singup-email').value;
    const password = document.querySelector('#singup-password').value;
    console.log(email,password)
    auth
        .createUserWithEmailAndPassword(email,password)
        .then(userCredential =>{
            console.log("El usuario ha sido creado");
            var user = userCredential.user
            console.log("el usuario es ${user}");
            signupForm.reset();
            $('#singupModal').modal('hide')
            

        })
})


signinForm.addEventListener('submit',(e) => {
    e.preventDefault();
    const email = document.querySelector('#login-email').value;
    const password = document.querySelector('#login-password').value;
    console.log(email,password)
    auth
        .signInWithEmailAndPassword(email,password)
        .then(userCredential =>{
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
            db
              .ref('users/' + userId).set({
                username: "holiss soy cristian 222",
                email: "myemail@user.com",
              
              });
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

 auth.onAuthStateChanged((user) =>{
   if (user){
     
  db.ref('users').child(globalId).on('value', function(snapshot) {
    var dato = snapshot.val();
    console.log("El dato leido es");
    console.log(dato);
    setupPosts(dato);
  });

    
//     console.log("estoy en if flag_ev");
  } 

 });

event_time =() =>{


  logok = 1;

  // stdata = db.ref();
  // stdata.child("users").child(globalId).get().then((snapshot) => {
  //   if (snapshot.exists()) {
  //     console.log(snapshot.val());
  //   } else {
  //     console.log("No data available");
  //   }
  // }).catch((error) => {
  //   console.error(error);
  // }); 
  console.log("jajajaja...");


};
//let mytimer = setInterval(event_time,10000);
// while((globalId != null)){
//   //console.log("estoy tratando de leer un dato");
//   var myCheck = db.ref('users/' + globalId );
  
//   myCheck.on('value', (snapshot) => {
//     const data = snapshot.val();
//     console.log("el dato leido es ");
//     console.log(data);
//   });
//   logok = 0;
      
// }


