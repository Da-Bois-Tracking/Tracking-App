import { useState, useEffect } from "react";
import { CountryDropdown, StateDropdown, CityDropdown, PhoneInput } from "react-country-state-dropdown";
import { CitySelect, CountrySelect, StateSelect, LanguageSelect, } from "react-country-state-city";


// interface User {
//     userName: string
// }

const Registration = () => {
    const [ userName, setUserName ] = useState("")
    const [ firstName, setFirstName ] = useState("")
    const [ lastName, setLastName ] = useState("")
    const [ email, setEmail ] = useState("")
    const [ password, setPassword ] = useState("")
    const [ confirmPassword, setConfirmPassword ] = useState("")
    const [ dob, setDob ] = useState("")
    const [ phoneNumber, setPhoneNumber ] = useState("")
    const [ country, setCountry ] = useState(0)
    const [ state, setState ] = useState(0)
    const [ city, setCity ] = useState(0)
    const [ weight, setWeight ] = useState("")
    const [ height, setHeight ] = useState("")
    const [ skillLevel, setSkillLevel ] = useState("")
    const [ position, setPosition ] = useState("")
    
    const handleSkill = (e) => {
        setSkillLevel(e.target.value)
    }

    const BASE_URL = "http://localhost:8000/"

    const handleRegistration = (e) => {
        e.preventDefault()

        if(password !== confirmPassword){
            alert("Passwords do not match!")
        } else {
            console.log(userName, firstName, lastName, email, password, confirmPassword, dob, phoneNumber, country, state, city, weight, height, skillLevel, position)
            let data = {userName, firstName, lastName, email, password, dob, phoneNumber, country, state, city, weight, height, skillLevel, position}
    
            fetch(`${BASE_URL}users/`, {
                method:"POST",
                headers:{
                    "accept":"application/json",
                    "Content-type":"application/json"
                },
                body:JSON.stringify(data)
            })
        }
    }


    return (
        <div>
            <h1>Registration</h1>
            <form>
                <input 
                    type="text"
                    placeholder="Username"
                    value={userName}
                    onChange={(e) => setUserName(e.target.value)} />
                <input 
                    type="text" 
                    placeholder="First Name"
                    value={firstName} 
                    onChange={(e) => setFirstName(e.target.value)} />
                <input 
                    type="text" 
                    placeholder="Last Name"
                    value={lastName} 
                    onChange={(e) => setLastName(e.target.value)} />
                <input 
                    type="email" 
                    placeholder="Email"
                    value={email} 
                    onChange={(e) => setEmail(e.target.value)} />
                <input 
                    type="password" 
                    placeholder="Password"
                    value={password} 
                    onChange={(e) => setPassword(e.target.value)} />
                <input 
                    type="password" 
                    placeholder="Confirm Password"
                    value={confirmPassword} 
                    onChange={(e) => setConfirmPassword(e.target.value)} />
                <label htmlFor="dob">Date of Birth: </label>
                <input 
                    type="date" 
                    value={dob} 
                    onChange={(e) => setDob(e.target.value)} />
                <PhoneInput 
                    clearable 
                    country={country} 
                    value={phoneNumber} 
                    onChange={(e) => setPhoneNumber(e.target.value)} />
                <CountrySelect
                    clearable 
                    value={country} 
                    onChange={(e) => setCountry(e.id)} 
                    placeHolder="Select Country"/>
                <StateSelect
                    clearable 
                    country={country} 
                    value={state} 
                    onChange={(e) => setState(e.id)} 
                    placeHolder="Select State" />
                <CitySelect
                    clearable 
                    allowFreeFormText 
                    country={country}
                    state={state} 
                    value={city} onChange={(e) => setCity(e.id)} 
                    placeHolder="Select City" />
                <input 
                    type="number" 
                    placeholder="Weight(kg)"
                    value={weight} 
                    onChange={(e) => setWeight(e.target.value)} />
                <input 
                    type="number" 
                    placeholder="Height(cm)"
                    value={height} 
                    onChange={(e) => setHeight(e.target.value)} />
                <label htmlFor="skill level">Skill Level</label>
                <select name="skill level" value={skillLevel} onChange={handleSkill}>
                    <option value="high school">High School</option>
                    <option value="college">College</option>
                    <option value="semi pro">Semi-pro</option>
                    <option value="professional">Professional</option>
                </select>
                <input 
                    type="text" 
                    placeholder="Position"
                    value={position} 
                    onChange={(e) => setPosition(e.target.value)} />
                <button type="submit" onClick={handleRegistration}>
                    Register
                </button>
            </form>
        </div>
    )
}

export default Registration