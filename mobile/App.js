import { Camera, CameraType } from 'expo-camera';
import { useState } from 'react';
import { Button, ScrollView, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { ImageBackground, Image } from 'react-native';
import { Chip, IconButton } from "@react-native-material/core";
import { useFonts } from 'expo-font';
import Icon from "@expo/vector-icons/MaterialCommunityIcons";
import Lottie from 'lottie-react-native';

export default function App() {
  let camera;
  const [type, setType] = useState(CameraType.back);
  const [permission, requestPermission] = Camera.useCameraPermissions();
  const [previewVisible, setPreviewVisible] = useState(false)
  const [capturedImage, setCapturedImage] = useState(false)
  const [showResults, setShowResults] = useState(false)
  const [apiResponse, setApiResponse] = useState({})
  const [isLoading, setIsLoading] = useState(false)
  const API_URL = 'http://10.0.10.70:8000/api/v1'

  if (!permission) {
    return (
      <View style={styles.container}>
        <Text>Permission is not granted</Text>
        <Button title="Request Permission" onPress={requestPermission} />
      </View>
    );
  }

  if (!permission.granted) {
    return (
      <View style={styles.container}>
        <Text>Permission is not granted</Text>
        <Button title="Request Permission" onPress={requestPermission} />
      </View>
    );
  }

  const __switchCamera = async () => {
    setType(current => (current === CameraType.back ? CameraType.front : CameraType.back));
  }

  const __retakePicture = () => {
    setCapturedImage(null)
    setPreviewVisible(false)
  }

  const __savePhoto = async () => {
    var data = new FormData()
    data.append('file', { uri: capturedImage.uri, name: 'image.jpg', type: 'image/jpeg' })
    setIsLoading(true)
    setShowResults(true)

    let response = await fetch(API_URL + '/recipe/fromImage', {
      method: 'POST',
      body: data
    })
    if (response.ok) {
      let recipeResult = await response.json()
      console.log(recipeResult)
      setApiResponse(recipeResult)
      setIsLoading(false)

    } else {
      console.error(response)
    }
  }

  const __takePicture = async () => {
    if (!camera) return
    const photo = await camera.takePictureAsync()
    setPreviewVisible(true)
    setCapturedImage(photo)
  }

  return (
    <View style={styles.container}>
      {previewVisible && capturedImage ?
        (!showResults ? <CameraPreview photo={capturedImage} retakePicture={__retakePicture} savePhoto={__savePhoto} /> : <ShowResults isLoading={isLoading} result={apiResponse} />)
        : (<Camera
          style={styles.camera}
          type={type}
          ref={(r) => {
            camera = r
          }}>
          <View style={styles.choices}>
            <ScrollView horizontal={true}>
              <RecipeChoice type="Vegan" icon="leaf" />
              <RecipeChoice type="Vegetarian" icon="carrot" />
              <RecipeChoice type="Gluten Free" icon="wheat" />
              <RecipeChoice type="Keto" icon="food-drumstick" />
              <RecipeChoice type="Paleo" icon="food-apple" />
              <RecipeChoice type="Low Carb" icon="food-apple" />
              <RecipeChoice type="Low Fat" icon="food-apple" />
            </ScrollView>
          </View>

          <View style={styles.cameraControls}>
            <View style={styles.buttonContainer}>
              <TouchableOpacity
                onPress={__takePicture}
                style={styles.takePhotoButton}
              />
            </View>
          </View>
        </Camera>)
      }
    </View>
  );
}

const ShowResults = ({ isLoading, result }) => {
  console.log(result)
  console.log('asda')
  const [loaded] = useFonts({Norms: require('./assets/fonts/TTNorms-Regular.otf'),
  Sister: require('./assets/fonts/Sisterhood.ttf'), });

  if (!loaded) {
  return null;
  }
  const API_URL = 'http://10.0.10.70:8000/api/v1'
  console.log((API_URL+'/recipe/image/'+result.image))

  return (
    <View>

      {isLoading ? 
        <View style={{ alignItems: 'center' }}>
          <Image source={require('./assets/animation_500_ljuhcncl.gif')} style={{width:300, height:300}} />
          <Text style={styles.resultTitle2}>Yemek tarifi bulunuyor</Text>
        </View>:

        <View style={styles.resultContainer}>
          <Text style={styles.resultTitle}>{result.recipe.name.toUpperCase()}</Text>
          <Image
            style={styles.food_image}
            source={{
              uri: (API_URL+'/recipe/image/'+result.image),
            }}
          />
          <ScrollView horizontal={false}>
          <Text style={styles.resultTitle2}>Malzemeler</Text>

          <View style={{ marginTop: 0 }}>
            {result.recipe.ingredients.map((item, index) => (
              <Text style={styles.ingredients}>{item}</Text>
            ))}

          </View>
          <View style={{ marginTop: 20 }}>
            <Text style={styles.resultTitle2}>Tarif</Text>
            <Text style={styles.instructions}>{result.recipe.instructions}</Text>
            
          </View>
          <Text style={styles.resultTitle2}>Afiyet Olsun</Text>

          </ScrollView>

        </View>
      }
    </View>
  )
}


const CameraPreview = ({ photo, retakePicture, savePhoto }) => {
  return (
    <View
      style={{
        backgroundColor: 'transparent',
        flex: 1,
        width: '100%',
        height: '100%'
      }}
    >
      <ImageBackground
        source={{ uri: photo && photo.uri }}
        style={{
          flex: 1
        }}
      >

        <View
          style={{
            flex: 1,
            flexDirection: 'column',
            padding: 15,
            justifyContent: 'flex-end'
          }}
        >
          <View
            style={{
              flexDirection: 'row',
              justifyContent: 'space-between'
            }}
          >
            <TouchableOpacity
              onPress={retakePicture}

              style={{
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                width: 80,
                height: 80,
                backgroundColor: 'transparent',
                borderRadius: 12,
                borderColor: '#fff',
                borderWidth: 2,
                marginLeft: 20,
                marginBottom: 50
              }}
            >
              <Icon name="camera-retake-outline" size={35} color="#fff" />
            </TouchableOpacity>
            <TouchableOpacity
              onPress={savePhoto}
              style={{
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                width: 80,
                height: 80,
                backgroundColor: 'transparent',
                borderRadius: 12,
                borderColor: '#fff',
                borderWidth: 2,
                marginRight: 20,
                marginBottom: 50
              }}
            >
              <Icon name="send" size={35} color="#fff" />


            </TouchableOpacity>
            
          </View>
          
        </View>

      </ImageBackground>
    </View>
  )
}


const RecipeChoice = ({ type, icon }) => {
  return (
    <View style={{
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      width: 80,
      height: 80,
      backgroundColor: 'transparent',
      borderRadius: 12,
      borderColor: '#fff',
      borderWidth: 2,
      margin: 5
    }}>
      <Icon name={icon} size={20} color="#fff" />
      <Text style={{ color: '#fff', marginLeft: 10 }}>{type}</Text>
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F7F5EC',
    alignItems: 'center',
    justifyContent: 'center',
  },
  cameraControls: {
    position: 'absolute',
    bottom: 0,
    flexDirection: 'row',
    flex: 1,
    width: '100%',
    padding: 20,
    justifyContent: 'space-between'
  },
  takePhotoButton: {
    width: 70,
    height: 70,
    bottom: 0,
    borderRadius: 50,
    marginBottom: 20,
    borderColor: '#ececec',
    borderWidth: 5,
    backgroundColor: '#dedede'
  },
  camera: {
    flex: 1,
    width: '100%',
  },
  text: {
    fontSize: 18,
    color: 'white',
  },
  buttonContainer: {
    alignSelf: 'center',
    flex: 1,
    alignItems: 'center'
  },
  choices: {
    position: 'absolute',
    bottom: 120,
    flexDirection: 'row',
    flex: 1,
    width: '100%',
    height: 100,
    justifyContent: 'space-between',
  },
  resultContainer: {
    flex: 1,
    // flexDirection: 'row',
    backgroundColor: '#F7F5EC',
    width: '100vw',
  },
  food_image: {
    width: 250,
    height: 250,
    alignSelf: 'center',
    marginTop: 20,
  },
  resultTitle: {
    color: '#D47D3B',
    fontSize: 25,
    lineHeight: 48,
    fontWeight: 'bold',
    textAlign: 'center',
    marginTop: 60,
    paddingRight: 15,
    paddingLeft: 15,
  },
  resultTitle2: {
    color: '#D47D3B',
    fontSize: 40,
    // lineHeight: 48,
    fontFamily: 'Sister',
    textAlign: 'center',
    marginTop: 0,
  },
  resultTitle3: {
    color: '#D47D3B',
    fontSize: 30,
    fontFamily: 'Sister',
    textAlign: 'right',
    marginRight: 40,
  },
  resultContainer: {
    flex: 1,
    flexDirection: 'column',
    backgroundColor: '#F7F5EC',
    width: '100%',
  },
  food_image: {
    width: 250,
    height: 250,
    alignSelf: 'center',
    marginTop: 20,
  },
  ingredients:  {
    color: '#56585B',
    fontSize: 14,
    lineHeight: 21,
    textAlign: 'center',
    fontFamily: 'Norms',

  },
  instructions:  {
    color: '#56585B',
    fontSize: 14,
    lineHeight: 21,
    textAlign: 'left',
    fontFamily: 'Norms',
    marginLeft: 25,
    marginRight: 25,
    marginBottom: 15
  },

});
