import { useState, useEffect } from "react";
import { CountryDropdown, StateDropdown, CityDropdown, PhoneInput } from "react-country-state-dropdown";

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
     const [ country, setCountry ] = useState("")
     const [ state, setState ] = useState("")
     const [ city, setCity ] = useState("")
     const [ weight, setWeight ] = useState("")
     const [ height, setHeight ] = useState("")
     const [ skillLevel, setSkillLevel ] = useState("")
     const [ position, setPosition ] = useState("")
    
     const handleSkill = (event) => {
        setSkillLevel(event.target.value)
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
                <CountryDropdown 
                    clearable 
                    value={country} 
                    onChange={(e) => setCountry(e.target.value)} />
                <StateDropdown 
                    clearable 
                    country={country} 
                    value={state} 
                    onChange={(e) => setState(e.target.value)} />
                <CityDropdown 
                    clearable 
                    allowFreeFormText 
                    country={country}
                    state={state} 
                    value={city} onChange={(e) => setCity(e.target.value)} />
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
            </form>
        </div>
     )
}

export default Registration