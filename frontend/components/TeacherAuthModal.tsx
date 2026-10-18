'use client';

import React, { useState, useEffect } from 'react';
import { 
  Sparkles, 
  GraduationCap, 
  School, 
  Mail, 
  Phone, 
  Lock, 
  User, 
  MapPin, 
  CheckCircle2, 
  ShieldCheck, 
  ArrowRight, 
  BookOpen,
  Zap,
  Eye,
  EyeOff
} from 'lucide-react';

export interface TeacherUser {
  id: string;
  name: string;
  school: string;
  city: string;
  email: string;
  whatsapp: string;
  primary_grade?: number;
  primary_subject?: string;
}

interface TeacherAuthModalProps {
  onAuthenticated: (user: TeacherUser) => void;
  isModal?: boolean;
}

export default function TeacherAuthModal({ onAuthenticated, isModal = true }: TeacherAuthModalProps) {
  const [mode, setMode] = useState<'signup' | 'login'>('signup');
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Form State
  const [name, setName] = useState('');
  const [school, setSchool] = useState('');
  const [city, setCity] = useState('');
  const [email, setEmail] = useState('');
  const [whatsapp, setWhatsapp] = useState('');
  const [password, setPassword] = useState('');
  const [primaryGrade, setPrimaryGrade] = useState<number>(10);
  const [primarySubject, setPrimarySubject] = useState<string>('Mathematics');

  // Login Form State
  const [loginIdentifier, setLoginIdentifier] = useState('');
  const [loginPassword, setLoginPassword] = useState('');

  // Check if educator previously registered or logged in
  useEffect(() => {
    try {
      const hasRegistered = localStorage.getItem('cbse_has_registered');
      const lastId = localStorage.getItem('cbse_last_identifier');
      if (hasRegistered === 'true' || lastId) {
        setMode('login');
        if (lastId) setLoginIdentifier(lastId);
      }
    } catch {}
  }, []);

  const handleSignup = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    if (!name.trim() || !school.trim() || !city.trim() || !email.trim() || !whatsapp.trim() || !password.trim()) {
      setError('Please fill in all required fields including password.');
      return;
    }

    if (password.trim().length < 4) {
      setError('Password must be at least 4 characters long.');
      return;
    }

    setLoading(true);
    try {
      const res = await fetch('/api/v1/auth/signup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: name.trim(),
          school: school.trim(),
          city: city.trim(),
          email: email.trim(),
          whatsapp: whatsapp.trim(),
          password: password,
          primary_grade: primaryGrade,
          primary_subject: primarySubject,
        }),
      });

      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.detail || 'Sign up failed. Please try again.');
      }

      const data = await res.json();
      const user: TeacherUser = data.user;
      localStorage.setItem('cbse_auth_teacher', JSON.stringify(user));
      localStorage.setItem('cbse_has_registered', 'true');
      localStorage.setItem('cbse_last_identifier', whatsapp.trim() || email.trim());
      onAuthenticated(user);
    } catch (err: any) {
      setError(err.message || 'An error occurred during registration.');
    } finally {
      setLoading(false);
    }
  };

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    if (!loginIdentifier.trim()) {
      setError('Please enter your email or WhatsApp number.');
      return;
    }

    if (!loginPassword.trim()) {
      setError('Please enter your account password.');
      return;
    }

    setLoading(true);
    try {
      const res = await fetch('/api/v1/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email_or_phone: loginIdentifier.trim(),
          password: loginPassword,
        }),
      });

      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.detail || 'Sign in failed.');
      }

      const data = await res.json();
      const user: TeacherUser = data.user;
      localStorage.setItem('cbse_auth_teacher', JSON.stringify(user));
      localStorage.setItem('cbse_has_registered', 'true');
      localStorage.setItem('cbse_last_identifier', loginIdentifier.trim());
      onAuthenticated(user);
    } catch (err: any) {
      setError(err.message || 'Could not sign in.');
    } finally {
      setLoading(false);
    }
  };

  const handleQuickDemo = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch('/api/v1/auth/demo');
      const data = await res.json();
      const user: TeacherUser = data.user;
      localStorage.setItem('cbse_auth_teacher', JSON.stringify(user));
      onAuthenticated(user);
    } catch {
      // Fallback local demo profile
      const demoUser: TeacherUser = {
        id: 'tch_demo_dps',
        name: 'Dr. Ananya Sharma',
        school: 'Delhi Public School, R.K. Puram',
        city: 'New Delhi',
        email: 'ananya.sharma@dps.edu.in',
        whatsapp: '+91 98765 43210',
        primary_grade: 10,
        primary_subject: 'Mathematics',
      };
      localStorage.setItem('cbse_auth_teacher', JSON.stringify(demoUser));
      onAuthenticated(demoUser);
    } finally {
      setLoading(false);
    }
  };

  const wrapperClasses = isModal
    ? "fixed inset-0 z-50 flex items-center justify-center bg-slate-900/70 p-4 backdrop-blur-md overflow-y-auto"
    : "w-full max-w-xl mx-auto";

  return (
    <div className={wrapperClasses}>
      <div className="relative w-full max-w-xl rounded-3xl bg-white shadow-2xl border border-slate-100 my-4 sm:my-8 overflow-hidden animate-in fade-in zoom-in-95 duration-200">
        {/* Header Ribbon */}
        <div className="bg-gradient-to-r from-blue-700 via-indigo-600 to-blue-800 px-6 py-6 text-white text-center relative">
          <div className="mx-auto mb-2 flex h-12 w-12 items-center justify-center rounded-2xl bg-white/10 backdrop-blur-md border border-white/20 shadow-inner">
            <GraduationCap className="h-6 w-6 text-white" />
          </div>
          <h2 className="text-xl sm:text-2xl font-black tracking-tight">
            CBSE Educator Verification Portal
          </h2>
          <p className="mt-1 text-xs sm:text-sm text-blue-100 font-medium max-w-md mx-auto">
            Sign up or log in to generate official CBSE Board exam papers, customize your school emblem, and save your question paper archive.
          </p>

          {/* Quick Demo Button */}
          <div className="mt-3.5">
            <button
              type="button"
              onClick={handleQuickDemo}
              disabled={loading}
              className="inline-flex items-center space-x-1.5 rounded-full bg-amber-400 px-3.5 py-1 text-xs font-black text-slate-950 shadow-md hover:bg-amber-300 transition-all active:scale-95 disabled:opacity-50"
            >
              <Zap className="h-3.5 w-3.5 fill-slate-950 text-slate-950" />
              <span>1-Click Educator Demo (Delhi Public School)</span>
            </button>
          </div>
        </div>

        {/* Tab Switcher */}
        <div className="flex border-b border-slate-200 bg-slate-50/80 px-6 pt-3">
          <button
            type="button"
            onClick={() => { setMode('login'); setError(null); }}
            className={`flex-1 pb-3 text-sm font-bold transition-all border-b-2 flex items-center justify-center space-x-1.5 ${
              mode === 'login'
                ? 'border-blue-600 text-blue-700'
                : 'border-transparent text-slate-500 hover:text-slate-800'
            }`}
          >
            <Lock className="h-4 w-4" />
            <span>Teacher Sign In (Log In)</span>
          </button>
          <button
            type="button"
            onClick={() => { setMode('signup'); setError(null); }}
            className={`flex-1 pb-3 text-sm font-bold transition-all border-b-2 flex items-center justify-center space-x-1.5 ${
              mode === 'signup'
                ? 'border-blue-600 text-blue-700'
                : 'border-transparent text-slate-500 hover:text-slate-800'
            }`}
          >
            <User className="h-4 w-4" />
            <span>Create Account (Sign Up)</span>
          </button>
        </div>

        {/* Body Content */}
        <div className="p-6">
          {error && (
            <div className="mb-4 rounded-xl bg-red-50 p-3 text-xs font-semibold text-red-700 border border-red-200 flex items-center space-x-2">
              <span className="h-2 w-2 rounded-full bg-red-500 shrink-0" />
              <span>{error}</span>
            </div>
          )}

          {mode === 'signup' ? (
            <form onSubmit={handleSignup} className="space-y-4">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
                {/* Full Name */}
                <div>
                  <label className="block text-xs font-bold text-slate-700 mb-1">
                    Teacher Full Name <span className="text-red-500">*</span>
                  </label>
                  <div className="relative">
                    <User className="absolute left-3 top-2.5 h-4 w-4 text-slate-400" />
                    <input
                      type="text"
                      required
                      placeholder="e.g. Dr. Ananya Sharma"
                      value={name}
                      onChange={(e) => setName(e.target.value)}
                      className="w-full rounded-xl border border-slate-200 pl-9 pr-3 py-2 text-xs font-medium text-slate-900 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                    />
                  </div>
                </div>

                {/* School Name */}
                <div>
                  <label className="block text-xs font-bold text-slate-700 mb-1">
                    School / Institution <span className="text-red-500">*</span>
                  </label>
                  <div className="relative">
                    <School className="absolute left-3 top-2.5 h-4 w-4 text-slate-400" />
                    <input
                      type="text"
                      required
                      placeholder="e.g. Delhi Public School"
                      value={school}
                      onChange={(e) => setSchool(e.target.value)}
                      className="w-full rounded-xl border border-slate-200 pl-9 pr-3 py-2 text-xs font-medium text-slate-900 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                    />
                  </div>
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
                {/* City */}
                <div>
                  <label className="block text-xs font-bold text-slate-700 mb-1">
                    City & State <span className="text-red-500">*</span>
                  </label>
                  <div className="relative">
                    <MapPin className="absolute left-3 top-2.5 h-4 w-4 text-slate-400" />
                    <input
                      type="text"
                      required
                      placeholder="e.g. New Delhi, Delhi"
                      value={city}
                      onChange={(e) => setCity(e.target.value)}
                      className="w-full rounded-xl border border-slate-200 pl-9 pr-3 py-2 text-xs font-medium text-slate-900 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                    />
                  </div>
                </div>

                {/* WhatsApp */}
                <div>
                  <label className="block text-xs font-bold text-slate-700 mb-1">
                    WhatsApp Number <span className="text-red-500">*</span>
                  </label>
                  <div className="relative">
                    <Phone className="absolute left-3 top-2.5 h-4 w-4 text-slate-400" />
                    <input
                      type="tel"
                      required
                      placeholder="+91 98765 43210"
                      value={whatsapp}
                      onChange={(e) => setWhatsapp(e.target.value)}
                      className="w-full rounded-xl border border-slate-200 pl-9 pr-3 py-2 text-xs font-medium text-slate-900 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                    />
                  </div>
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
                {/* Email */}
                <div>
                  <label className="block text-xs font-bold text-slate-700 mb-1">
                    Official Email <span className="text-red-500">*</span>
                  </label>
                  <div className="relative">
                    <Mail className="absolute left-3 top-2.5 h-4 w-4 text-slate-400" />
                    <input
                      type="email"
                      required
                      placeholder="ananya.sharma@dps.edu.in"
                      value={email}
                      onChange={(e) => setEmail(e.target.value)}
                      className="w-full rounded-xl border border-slate-200 pl-9 pr-3 py-2 text-xs font-medium text-slate-900 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                    />
                  </div>
                </div>

                {/* Password */}
                <div>
                  <label className="block text-xs font-bold text-slate-700 mb-1">
                    Create Password <span className="text-red-500">*</span>
                  </label>
                  <div className="relative">
                    <Lock className="absolute left-3 top-2.5 h-4 w-4 text-slate-400" />
                    <input
                      type={showPassword ? 'text' : 'password'}
                      required
                      minLength={4}
                      placeholder="Min. 4 characters"
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                      className="w-full rounded-xl border border-slate-200 pl-9 pr-9 py-2 text-xs font-medium text-slate-900 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                    />
                    <button
                      type="button"
                      onClick={() => setShowPassword(!showPassword)}
                      className="absolute right-3 top-2.5 text-slate-400 hover:text-slate-600"
                    >
                      {showPassword ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                    </button>
                  </div>
                </div>
              </div>

              {/* Teaching Scope Preferences */}
              <div className="grid grid-cols-2 gap-3.5 bg-slate-50 p-3 rounded-2xl border border-slate-200">
                <div>
                  <label className="block text-[11px] font-bold text-slate-600 mb-1">Primary Class</label>
                  <select
                    value={primaryGrade}
                    onChange={(e) => setPrimaryGrade(Number(e.target.value))}
                    className="w-full rounded-lg border border-slate-300 bg-white px-2.5 py-1.5 text-xs font-bold text-slate-800"
                  >
                    <option value={10}>Class 10 (Secondary)</option>
                    <option value={11}>Class 11 (Senior Secondary)</option>
                    <option value={12}>Class 12 (Senior Secondary)</option>
                  </select>
                </div>
                <div>
                  <label className="block text-[11px] font-bold text-slate-600 mb-1">Subject</label>
                  <select
                    value={primarySubject}
                    onChange={(e) => setPrimarySubject(e.target.value)}
                    className="w-full rounded-lg border border-slate-300 bg-white px-2.5 py-1.5 text-xs font-bold text-slate-800"
                  >
                    <option value="Mathematics">Mathematics</option>
                    <option value="Science">Science (Physics / Chem / Bio)</option>
                    <option value="Physics">Physics</option>
                    <option value="Chemistry">Chemistry</option>
                    <option value="Biology">Biology</option>
                    <option value="English">English</option>
                    <option value="Social Science">Social Science</option>
                  </select>
                </div>
              </div>

              {/* Submit Button */}
              <button
                type="submit"
                disabled={loading}
                className="w-full rounded-2xl bg-blue-600 py-3 text-xs sm:text-sm font-black text-white shadow-lg shadow-blue-500/25 hover:bg-blue-700 transition-all active:scale-[0.99] flex items-center justify-center space-x-2 disabled:opacity-50"
              >
                <span>{loading ? 'Creating Educator Account...' : 'Complete Teacher Sign Up & Enter Studio'}</span>
                <ArrowRight className="h-4 w-4" />
              </button>

              <div className="text-center text-xs text-slate-500 pt-2">
                Already registered on this portal?{' '}
                <button
                  type="button"
                  onClick={() => { setMode('login'); setError(null); }}
                  className="font-bold text-blue-600 hover:underline"
                >
                  Sign In to your account
                </button>
              </div>
            </form>
          ) : (
            <form onSubmit={handleLogin} className="space-y-4">
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">
                  Email Address or WhatsApp Number <span className="text-red-500">*</span>
                </label>
                <div className="relative">
                  <Mail className="absolute left-3 top-2.5 h-4 w-4 text-slate-400" />
                  <input
                    type="text"
                    required
                    placeholder="e.g. +91 78289 02970 or teacher@school.edu"
                    value={loginIdentifier}
                    onChange={(e) => setLoginIdentifier(e.target.value)}
                    className="w-full rounded-xl border border-slate-200 pl-9 pr-3 py-2 text-xs font-medium text-slate-900 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                  />
                </div>
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">
                  Account Password <span className="text-red-500">*</span>
                </label>
                <div className="relative">
                  <Lock className="absolute left-3 top-2.5 h-4 w-4 text-slate-400" />
                  <input
                    type={showPassword ? 'text' : 'password'}
                    required
                    placeholder="Enter your password"
                    value={loginPassword}
                    onChange={(e) => setLoginPassword(e.target.value)}
                    className="w-full rounded-xl border border-slate-200 pl-9 pr-9 py-2 text-xs font-medium text-slate-900 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-3 top-2.5 text-slate-400 hover:text-slate-600"
                  >
                    {showPassword ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                  </button>
                </div>
              </div>

              <button
                type="submit"
                disabled={loading}
                className="w-full rounded-2xl bg-blue-600 py-3 text-xs sm:text-sm font-black text-white shadow-lg shadow-blue-500/25 hover:bg-blue-700 transition-all active:scale-[0.99] flex items-center justify-center space-x-2 disabled:opacity-50"
              >
                <span>{loading ? 'Authenticating...' : 'Sign In as Teacher'}</span>
                <ArrowRight className="h-4 w-4" />
              </button>

              <div className="text-center text-xs text-slate-500 pt-2">
                First time using CBSE PaperGen?{' '}
                <button
                  type="button"
                  onClick={() => { setMode('signup'); setError(null); }}
                  className="font-bold text-blue-600 hover:underline"
                >
                  Create New Teacher Account
                </button>
              </div>
            </form>
          )}

          {/* Trust Guarantees */}
          <div className="mt-5 grid grid-cols-3 gap-2 text-center border-t border-slate-100 pt-4 text-[10px] font-semibold text-slate-500">
            <div className="flex flex-col items-center">
              <ShieldCheck className="h-4 w-4 text-emerald-600 mb-0.5" />
              <span>CBSE Curriculum 2026-27</span>
            </div>
            <div className="flex flex-col items-center">
              <Sparkles className="h-4 w-4 text-blue-600 mb-0.5" />
              <span>Typst Print Engine</span>
            </div>
            <div className="flex flex-col items-center">
              <BookOpen className="h-4 w-4 text-purple-600 mb-0.5" />
              <span>Full Paper History</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
